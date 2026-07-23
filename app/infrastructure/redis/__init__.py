from app.infrastructure.redis.client import RedisClient

redis_client = RedisClient()

__all__ = ["redis_client"]