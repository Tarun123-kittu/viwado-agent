from contextlib import asynccontextmanager
from app.core.logging import configure_logging, logger
from app.infrastructure.http import http_client
from app.infrastructure.redis import redis_client

from fastapi import FastAPI


@asynccontextmanager
async def lifespan(app: FastAPI):
    configure_logging()

    # logger.info("Application starting")
    await http_client.start()
    await redis_client.start()

    yield

    # logger.info("Application shutting down")
    await redis_client.stop()
    await http_client.stop()