from contextlib import asynccontextmanager
from app.core.logging import configure_logging, logger

from fastapi import FastAPI


@asynccontextmanager
async def lifespan(app: FastAPI):
    configure_logging()

    logger.info("Application starting")

    yield

    logger.info("Application shutting down")