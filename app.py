from llm_client import LLMClient, FinishReason, ChatMessage

def main(client: LLMClient):
    messages: list[ChatMessage] = []

    print("Bimo iniciado :) Digite /sair para encerrar.\n")

    while True:
        try:
            message = input("Você: ").strip()
        except EOFError:
            print("\nEncerrando conversa.")
            break

        if message.lower() in {"/sair", "/exit", "/quit"}:
            print("Bimo: Até mais! :)\n")
            break

        if not message:
            continue

        messages.append(ChatMessage(role="user", content=message))

        result = client.chat(messages)

        print(f"Bimo: {result.text}")

        if result.finish_reason == FinishReason.LENGTH_LIMIT:
            print("\n[AVISO] A resposta pode estar incompleta devido ao limite de geração.")
        elif result.finish_reason == FinishReason.UNKNOWN:
                print("\n[AVISO] Não foi possível determinar o motivo de encerramento.")

        # Preserva a resposta no histórico da sessão, mesmo se ela tiver sido interrompida
        messages.append(
             ChatMessage(role="assistant", content=result.text)
        )

        print()







   
        
    