from fastapi import FastAPI

from app.api.router import api_router
from app.core.config import get_settings
from app.core.lifespan import lifespan
from app.core.exceptions.base import AppException
from app.core.exceptions.handlers import app_exception_handler
from app.api.middleware.request_id import RequestIDMiddleware


def create_app() -> FastAPI:
    """Create and configure the FastAPI application."""

    settings = get_settings()

    app = FastAPI(
        title=settings.app.name,
        version=settings.app.version,
        debug=settings.app.debug,
        lifespan=lifespan,
        docs_url="/docs" if settings.api.docs_enabled else None,
        redoc_url="/redoc" if settings.api.docs_enabled else None,
    )

    app.include_router(api_router)


    app.add_exception_handler(
        AppException,
        app_exception_handler,
    )

    app.add_middleware(RequestIDMiddleware)

    return app