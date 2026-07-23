from app.ai.llm.base import BaseLLM


class LLMProvider:

    def __init__(self, llm: BaseLLM):
        self._llm = llm

    async def generate(
        self,
        prompt: str,
        system: str | None = None,
    ) -> str:

        return await self._llm.generate(
            prompt,
            system,
        )