from qdrant_client import QdrantClient

from app.core.config import settings
from app.infrastructure.base import InfrastructureComponent


class QdrantClientManager(InfrastructureComponent):

    def __init__(self) -> None:
        self._client: QdrantClient | None = None

    async def start(self) -> None:
        
        self._client = QdrantClient(
            host=settings.qdrant.host,
            port=settings.qdrant.port,
            api_key=settings.qdrant.api_key or None,
        )

        self._client.get_collections()

    async def stop(self) -> None:
        self._client = None

    async def health(self) -> dict:

        if self._client is None:
            return {"status": "not_initialized"}

        try:
            self._client.get_collections()

            return {
                "status": "healthy"
            }

        except Exception as ex:
            return {
                "status": "unhealthy",
                "error": str(ex)
            }

    @property
    def client(self) -> QdrantClient:

        if self._client is None:
            raise RuntimeError(
                "Qdrant client is not initialized."
            )

        return self._client