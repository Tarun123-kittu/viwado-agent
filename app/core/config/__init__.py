from app.core.config.loader import get_settings

settings = get_settings()

__all__ = [
    "get_settings",
    "settings",
]