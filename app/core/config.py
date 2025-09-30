"""Application configuration settings."""
from functools import lru_cache
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_name: str = "ArmenianWhisper API"
    version: str = "0.1.0"
    cors_allow_origins: list[str] = ["http://localhost:5173", "http://127.0.0.1:5173"]
    max_upload_size_mb: int = 200

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


@lru_cache
def get_settings() -> Settings:
    return Settings()


settings = get_settings()
