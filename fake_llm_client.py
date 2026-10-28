from llm_client import (
    FinishReason,
    GenerationResult,
    LLMClient
    )

class FakeLLMClient:
    def chat(self, message: str) -> GenerationResult:
        return GenerationResult(
            text = f"Resposta simulada para: {message}",
            finish_reason=FinishReason.COMPLETED,
        )