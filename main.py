from llm_client import LLMClient
from ollama_client import OllamaClient

def main(client: LLMClient):
    answer = client.chat("Explique em uma frase o que é um agente de IA.")
    print(answer)


if __name__ == "__main__":
    main(OllamaClient())
