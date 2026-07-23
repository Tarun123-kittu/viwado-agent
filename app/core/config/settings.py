from app.core.config.api import APISettings
from app.core.config.app import AppSettings
from app.core.config.redis import RedisSettings
from app.core.config.qdrant import QdrantSettings
from app.core.config.llm import LLMSettings


class Settings:
    """Application settings container."""

    def __init__(self) -> None:
        self.app = AppSettings()
        self.api = APISettings()
        self.redis = RedisSettings()
        self.qdrant = QdrantSettings()
        self.llm = LLMSettings()