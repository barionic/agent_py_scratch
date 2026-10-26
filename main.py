import os

from app import main
from ollama_client import OllamaClient
from fake_llm_client import FakeLLMClient

def create_client():
    provider = os.getenv("LLM_PROVIDER", "ollama").lower()
    model = os.getenv("LLM_MODEL", "qwen3.5:0.8b")

    if provider == "ollama":
        return OllamaClient(model=model)

    if provider == "fake":
        return FakeLLMClient()

    raise ValueError(f"Provedor de LLM desconhecido: {provider}")

if __name__ == "__main__":
    main(create_client())