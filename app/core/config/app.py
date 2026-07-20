from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict

class AppSettings(BaseSettings):
    """Application configuration."""

    model_config = SettingsConfigDict(env_prefix="APP_",extra="ignore",)

    name: str = Field(default="Vewado AI Platform")
    version: str = Field(default="1.0.0")
    environment: str = Field(default="development")
    debug: bool = Field(default=True)