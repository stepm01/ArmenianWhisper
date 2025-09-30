"""FastAPI application entry point for ArmenianWhisper."""
from fastapi import FastAPI

from .api import router as api_router
from .core.config import settings


def create_app() -> FastAPI:
    app = FastAPI(
        title=settings.app_name,
        version=settings.version,
        description="REST API for ArmenianWhisper transcription and translation pipeline.",
    )
    app.include_router(api_router, prefix="/api")
    return app


app = create_app()
