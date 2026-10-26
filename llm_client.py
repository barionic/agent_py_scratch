from typing import Protocol

class LLMClient(Protocol):
    def chat(self, message: str) -> str:
        ...