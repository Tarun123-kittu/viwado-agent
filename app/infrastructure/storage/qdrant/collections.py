from qdrant_client.http.models import Distance, VectorParams
from qdrant_client.models import CollectionInfo

from app.core.config import settings
from app.infrastructure.storage.qdrant import QdrantClientManager


class QdrantCollectionManager:
    """Manage Qdrant collections."""

    def __init__(self, client: QdrantClientManager):
        self._client = client.client

    def exists(self) -> bool:
        collections = self._client.get_collections()

        return any(
            collection.name == settings.qdrant.collection
            for collection in collections.collections
        )

    def create(self, vector_size: int) -> None:

        if self.exists():
            return

        self._client.create_collection(
            collection_name=settings.qdrant.collection,
            vectors_config=VectorParams(
                size=vector_size,
                distance=Distance.COSINE,
            ),
        )

    def delete(self) -> None:

        if not self.exists():
            return

        self._client.delete_collection(
            settings.qdrant.collection
        )

    def info(self) -> CollectionInfo:

        return self._client.get_collection(
            settings.qdrant.collection
        )
    