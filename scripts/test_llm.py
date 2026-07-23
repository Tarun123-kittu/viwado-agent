from pathlib import Path
import sys
import asyncio

sys.path.append(str(Path(__file__).resolve().parent.parent))

from app.infrastructure.llm.ollama import OllamaLLM


async def main():

    llm = OllamaLLM()

    response = await llm.generate(
        prompt="write program that will calculate the sum of two numbers in python",
    )

    print(response)


asyncio.run(main())