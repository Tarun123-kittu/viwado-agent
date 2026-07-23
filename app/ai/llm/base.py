from abc import ABC, abstractmethod


class BaseLLM(ABC):

    @abstractmethod
    async def generate(
        self,
        prompt: str,
        system: str | None = None,
    ) -> str:
        pass