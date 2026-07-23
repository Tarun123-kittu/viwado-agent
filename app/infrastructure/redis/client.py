from redis.asyncio import Redis

from app.core.config import settings
from app.infrastructure.base import InfrastructureComponent


class RedisClient(InfrastructureComponent):
    """Application-wide Redis client."""

    def __init__(self) -> None:
        self._client: Redis | None = None

    async def start(self) -> None:
        self._client = Redis(
            host=settings.redis.host,
            port=settings.redis.port,
            db=settings.redis.db,
            password=settings.redis.password or None,
            decode_responses=True,
        )

        # Verify the connection on startup
        await self._client.ping()

    async def stop(self) -> None:
        if self._client is not None:
            await self._client.aclose()

    async def health(self) -> dict:
        if self._client is None:
            return {
                "service": "redis",
                "status": "not_started",
            }

        try:
            await self._client.ping()

            return {
                "service": "redis",
                "status": "healthy",
            }
        except Exception:
            return {
                "service": "redis",
                "status": "unhealthy",
            }

    @property
    def client(self) -> Redis:
        if self._client is None:
            raise RuntimeError("Redis client has not been initialized.")

        return self._client