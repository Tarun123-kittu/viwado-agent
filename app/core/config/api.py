from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class APISettings(BaseSettings):
    """API configuration."""

    model_config = SettingsConfigDict(
        env_prefix="API_",
        extra="ignore",
    )

    host: str = Field(default="0.0.0.0")
    port: int = Field(default=8000)
    reload: bool = Field(default=True)

    docs_enabled: bool = Field(default=True)

    stream_chunk_size: int = Field(default=1024)