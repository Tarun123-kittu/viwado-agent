from functools import lru_cache

from app.core.config.settings import Settings


@lru_cache
def get_settings() -> Settings:
    """Return the shared Settings instance."""
    return Settings()