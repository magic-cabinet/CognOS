from fastapi import APIRouter, UploadFile, File, HTTPException
from pydantic import BaseModel
# from services.minio_service import minio_service
from core_api.services.minio_service import minio_service
from pathlib import Path
import uuid

router = APIRouter()


class UploadResponse(BaseModel):
    id: str
    filename: str
    size: int
    url: str

class FileInfo(BaseModel):
    name: str
    size: int
    last_modified: str

@router.get("/")
async def list_files() -> list[FileInfo]:
    files = minio_service.list_files()
    return [
        FileInfo(
            name=obj.object_name,
            size=obj.size,
            last_modified=obj.last_modified.isoformat(),
        )
        for obj in files
    ]

@router.post("/", status_code=201)
async def upload_file(file: UploadFile = File(...)) -> UploadResponse:
    file_id = str(uuid.uuid4())
    content = await file.read()
    extension = Path(file.filename or "").suffix.lstrip(".") or "bin"
    stored_name = f"{file_id}.{extension}"

    minio_service.upload(stored_name, content, file.content_type or "application/octet-stream")

    return UploadResponse(
        id=file_id,
        filename=file.filename or "unknown",
        size=len(content),
        url=minio_service.get_url(stored_name),
    )


@router.get("/{file_id}")
async def get_file(file_id: str):
    try:
        url = minio_service.get_url(file_id)
        return {"id": file_id, "url": url}
    except Exception:
        raise HTTPException(404, "File not found")


@router.delete("/{file_id}", status_code=204)
async def delete_file(file_id: str):
    try:
        minio_service.delete(file_id)
    except Exception:
        raise HTTPException(404, "File not found")