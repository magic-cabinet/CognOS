from flask import Blueprint, request, jsonify, send_file
from api.minio_client import get_minio_client
from io import BytesIO

upload_bp = Blueprint("upload", __name__, url_prefix="/upload")

# ------------------------------
# LIST ALL FILES IN BUCKET
# ------------------------------
@upload_bp.route("/list", methods=["GET"])
def list_files():
    client = get_minio_client()
    bucket_name = "documents"

    # Create bucket if not exists
    if not client.bucket_exists(bucket_name):
        client.make_bucket(bucket_name)

    objects = client.list_objects(bucket_name, recursive=True)

    files = [obj.object_name for obj in objects]

    return jsonify({"files": files})

# ------------------------------
# GET A FILE AS BYTES
# ------------------------------
@upload_bp.route("/get/<path:filename>", methods=["GET"])
def get_file(filename):
    client = get_minio_client()
    bucket_name = "documents"

    try:
        minio_obj = client.get_object(bucket_name, filename)

        # Read into memory
        file_bytes = minio_obj.read()

        return send_file(
            BytesIO(file_bytes),
            download_name=filename,
            mimetype="application/octet-stream"
        )

    except Exception as e:
        return jsonify({"error": str(e)}), 404


# ------------------------------
# UPLOAD A FILE
# ------------------------------
@upload_bp.route("/upload", methods=["POST"])
def upload_file():
    if "file" not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    file = request.files["file"]
    original_filename = file.filename

    # NEW: optional override name
    upload_as = request.form.get("upload_as", original_filename)

    client = get_minio_client()
    bucket_name = "documents"

    # Create bucket if not exists
    if not client.bucket_exists(bucket_name):
        client.make_bucket(bucket_name)

    # Upload with the chosen name
    client.put_object(
        bucket_name=bucket_name,
        object_name=upload_as,
        data=file,
        length=-1,  # unknown length stream
        part_size=10 * 1024 * 1024,
    )

    return jsonify({
        "status": "success",
        "original_file_name": original_filename,
        "stored_as": upload_as,
        "url": f"http://localhost:9000/{bucket_name}/{upload_as}"
    })