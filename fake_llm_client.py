from llm_client import LLMClient

class FakeLLMClient:
    def chat(self, message: str) -> str:
        return f"Resposta simulada para: {message}"