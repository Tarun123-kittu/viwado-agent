from abc import ABC, abstractmethod


class InfrastructureComponent(ABC):
    """Base class for infrastructure components."""

    @abstractmethod
    async def start(self) -> None:
        """Start the component."""
        ...

    @abstractmethod
    async def stop(self) -> None:
        """Stop the component."""
        ...

    @abstractmethod
    async def health(self) -> dict:
        """Return component health."""
        ...