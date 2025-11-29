from minio import Minio
import os

def get_minio_client() -> Minio:
    return Minio(
        os.getenv("MINIO_ENDPOINT", "minio:9000"),
        access_key=os.getenv("MINIO_ROOT_USER", "admin"),
        secret_key=os.getenv("MINIO_ROOT_PASSWORD", "admin123"),
        secure=False
    )
