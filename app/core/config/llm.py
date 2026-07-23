from pydantic_settings import BaseSettings, SettingsConfigDict


class LLMSettings(BaseSettings):
    """LLM configuration."""

    host: str = "http://localhost:11434"

    model: str = "llama3.1:8b"

    temperature: float = 0.2

    model_config = SettingsConfigDict(
        env_prefix="LLM_",
        extra="ignore",
    )