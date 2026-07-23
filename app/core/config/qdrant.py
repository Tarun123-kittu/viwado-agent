from pydantic_settings import BaseSettings, SettingsConfigDict


class QdrantSettings(BaseSettings):
    """Qdrant configuration."""

    host: str = "localhost"
    port: int = 6333
    api_key: str = ""
    collection: str = "knowledge_base"

    model_config = SettingsConfigDict(
        env_prefix="QDRANT_",
        extra="ignore",
    )