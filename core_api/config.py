# from pydantic_settings import BaseSettings
import os

# class Settings(BaseSettings):
class Settings:
    redis_host: str = "redis"
    redis_port: int = 6379
    # minio_endpoint: str = "minio:9000"
    minio_endpoint: str = os.getenv("MINIO_ENDPOINT", "localhost:9000") 
    minio_root_user: str = "admin"
    minio_root_password: str = "admin123"
    minio_bucket: str = "documents"
    minio_secure: bool = False


    @property
    def redis_url(self) -> str:
        return f"redis://{self.redis_host}:{self.redis_port}"

    class Config:
        env_file = ".env"


settings = Settings()