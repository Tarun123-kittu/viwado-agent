from dataclasses import dataclass


@dataclass(slots=True)
class GenerationRequest:
    prompt: str
    system: str | None = None


@dataclass(slots=True)
class GenerationResponse:
    text: str