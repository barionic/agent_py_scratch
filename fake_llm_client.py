from llm_client import (
    ChatMessage,
    FinishReason,
    GenerationResult,
    LLMClient
    )

class FakeLLMClient:
    def __init__(
        self, 
        finish_reason: FinishReason = FinishReason.COMPLETED
    ):
        self.finish_reason = finish_reason
        self.received_histories: list[list[ChatMessage]] = [] 

    def chat(self, messages: list[ChatMessage]) -> GenerationResult:
        #Guarda uma cópia do histórico recebido para os testes.
        self.received_histories.append(list(messages))

        last_user_message = next(
            message
            for message in reversed(messages)
            if message.role == "user"
        )

        return GenerationResult(
            text = f"Resposta simulada para: {last_user_message.content}",
            finish_reason=self.finish_reason,
        )