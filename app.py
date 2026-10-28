from llm_client import LLMClient

def main(client: LLMClient):
    #answer = client.chat("Explique em uma frase o que é um agente de IA.")
    message = input("Você: ")
    result = client.chat(message)

    print(result.text)
    print(f"\nMotivo do encerramento: {result.finish_reason.value}")