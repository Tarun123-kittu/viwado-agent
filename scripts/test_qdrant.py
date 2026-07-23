from pathlib import Path
import sys

sys.path.append(str(Path(__file__).resolve().parent.parent))

import asyncio

from app.infrastructure.storage.qdrant import (
    QdrantClientManager,
    QdrantCollectionManager,
)

async def main():

    client = QdrantClientManager()

    await client.start()

    manager = QdrantCollectionManager(client)

    manager.create(vector_size=1024)

    print(manager.exists())

    print(manager.info())

    await client.stop()


asyncio.run(main()) 