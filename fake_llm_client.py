from llm_client import (
    FinishReason,
    GenerationResult,
    LLMClient
    )

class FakeLLMClient:
    def __init__(self, finish_reason: FinishReason = FinishReason.COMPLETED):
        self.finish_reason = finish_reason

    def chat(self, message: str) -> GenerationResult:
        return GenerationResult(
            text = f"Resposta simulada para: {message}",
            finish_reason=self.finish_reason,
        )