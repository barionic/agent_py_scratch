from llm_client import LLMClient, FinishReason

def main(client: LLMClient):
    #answer = client.chat("Explique em uma frase o que é um agente de IA.")
    message = input("Você: ")
    result = client.chat(message)

    print(result.text)

    if result.finish_reason == FinishReason.LENGTH_LIMIT:
        print("\n[AVISO] A resposta pode estar incompleta devido ao limite de geração.")
    elif result.finish_reason == FinishReason.UNKNOWN:
        print("\n[AVISO] Não foi possível determinar o motivo de encerramento.")