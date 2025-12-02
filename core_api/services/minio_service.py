from minio import Minio
from minio.error import S3Error
from core_api.config import settings
from datetime import timedelta
import io


class MinioService:
    def __init__(self):
        self._client: Minio | None = None

    def connect(self):
        self._client = Minio(
            # settings.minio_endpoint,
            # "minio:9000",
            settings.minio_endpoint,
            access_key=settings.minio_root_user,
            secret_key=settings.minio_root_password,
            # secure=settings.minio_secure,
            secure=False
        )
        if not self._client.bucket_exists(settings.minio_bucket):
            self._client.make_bucket(settings.minio_bucket)
        print("connected")

    def upload(self, file_name: str, data: bytes, content_type: str) -> str:
        self._client.put_object(
            settings.minio_bucket,
            file_name,
            io.BytesIO(data),
            length=len(data),
            content_type=content_type,
        )
        return file_name

    def download(self, file_name: str) -> bytes:
        response = self._client.get_object(settings.minio_bucket, file_name)
        return response.read()

    def delete(self, file_name: str):
        self._client.remove_object(settings.minio_bucket, file_name)

    def get_url(self, file_name: str, expires: int = 3600) -> str:
        return self._client.presigned_get_object(
            settings.minio_bucket, file_name, expires=timedelta(seconds=expires)
        )

    def list_files(self, prefix: str = "", recursive: bool = True):
        return list(self._client.list_objects(
            settings.minio_bucket,
            prefix=prefix,
            recursive=recursive,
        ))


minio_service = MinioService()
# minio_service.connect()