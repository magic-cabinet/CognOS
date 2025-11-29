from flask import Blueprint, request, jsonify
from api.minio_client import get_minio_client

upload_bp = Blueprint("upload", __name__, url_prefix="/upload")

@upload_bp.route("/upload", methods=["POST"])
def upload_file():
    if "file" not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    file = request.files["file"]
    filename = file.filename

    client = get_minio_client()

    bucket_name = "documents"

    # Create bucket if not exists
    if not client.bucket_exists(bucket_name):
        client.make_bucket(bucket_name)

    # Upload
    client.put_object(
        bucket_name=bucket_name,
        object_name=filename,
        data=file,
        length=-1,  # stream without knowing length
        part_size=10 * 1024 * 1024,
    )

    return jsonify({
        "status": "success",
        "file_name": filename,
        "url": f"http://localhost:9000/{bucket_name}/{filename}"
    })
