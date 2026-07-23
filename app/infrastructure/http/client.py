import httpx
from app.infrastructure.base import InfrastructureComponent

class HTTPClient(InfrastructureComponent):
    """Application-wide HTTP client."""

    def __init__(self) -> None:
        self._client: httpx.AsyncClient | None = None

    async def start(self) -> None:
        """Initialize the HTTP client."""

        self._client = httpx.AsyncClient(
            timeout=httpx.Timeout(
                timeout=30.0,
                connect=10.0,
            ),
            follow_redirects=True,
        )

    async def stop(self) -> None:
        """Shutdown the HTTP client."""

        if self._client is not None:
            await self._client.aclose()

    @property
    def client(self) -> httpx.AsyncClient:
        if self._client is None:
            raise RuntimeError("HTTP client has not been initialized.")

        return self._client
    
    async def health(self) -> dict:
        return {
            "service": "http",
            "status": "healthy" if self._client else "not_started",
        }