from contextlib import asynccontextmanager
from fastapi import FastAPI
from cognos.core_api.services.redis_service import redis_service
from cognos.core_api.services.minio_service import minio_service


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup
    await redis_service.connect()
    print("getting redis client")
    minio_service.connect()
    print("getting minio client")
    print("🌍 CognOS API started")
    yield
    # Shutdown
    await redis_service.disconnect()
    print("🛑 CognOS API shutting down")