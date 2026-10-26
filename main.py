from ollama_client import chat

def main():
    answer = chat("Explique em uma frase o que é um agente de IA.")
    print(answer)


if __name__ == "__main__":
    main()
