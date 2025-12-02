from redis.asyncio import Redis
from core_api.config import settings


class RedisService:
    def __init__(self):
        self._client: Redis | None = None

    async def connect(self):
        # self._client = Redis.from_url(settings.redis_url, decode_responses=True)
        self._client = Redis(
            host="localhost",
            port=6379,
            decode_responses=True
        )


    async def disconnect(self):
        if self._client:
            await self._client.close()

    async def get(self, key: str) -> str | None:
        return await self._client.get(key)

    async def set(self, key: str, value: str, ttl: int | None = None):
        await self._client.set(key, value, ex=ttl)

    async def delete(self, key: str):
        await self._client.delete(key)


redis_service = RedisService()