from app import main
from ollama_client import OllamaClient
from fake_llm_client import FakeLLMClient

if __name__ == "__main__":
    main(OllamaClient())
    #main(FakeLLMClient())
