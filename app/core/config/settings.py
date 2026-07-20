from app.core.config.api import APISettings
from app.core.config.app import AppSettings


class Settings:
    """Application settings container."""

    def __init__(self) -> None:
        self.app = AppSettings()
        self.api = APISettings()