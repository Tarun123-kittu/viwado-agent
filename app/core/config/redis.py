from pydantic_settings import BaseSettings, SettingsConfigDict


class RedisSettings(BaseSettings):
    """Redis configuration."""

    host: str = "localhost"
    port: int = 6379
    db: int = 0
    password: str = ""

    model_config = SettingsConfigDict(
        env_prefix="REDIS_",
        extra="ignore",
    )