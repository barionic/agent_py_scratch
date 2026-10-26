from llm_client import LLMClient

def main(client: LLMClient):
    answer = client.chat("Explique em uma frase o que é um agente de IA.")
    print(answer)
