from ollama import AsyncClient

from app.ai.llm.base import BaseLLM
from app.core.config import settings


class OllamaLLM(BaseLLM):

    def __init__(self):

        self._client = AsyncClient(
            host=settings.llm.host
        )

    async def generate(
        self,
        prompt: str,
        system: str | None = None,
    ) -> str:

        response = await self._client.chat(
            model=settings.llm.model,
            messages=[
                *(
                    [{
                        "role": "system",
                        "content": system,
                    }]
                    if system
                    else []
                ),
                {
                    "role": "user",
                    "content": prompt,
                },
            ],
            options={
                "temperature": settings.llm.temperature,
            },
        )

        return response["message"]["content"]