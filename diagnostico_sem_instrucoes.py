import json
from time import perf_counter
from urllib.request import Request, urlopen

payload = {
    "model": "qwen3.5:0.8b",
    "messages": [
        {
            "role": "user",
            "content": "Quem é você? Qual é seu propósito?",
        }
    ],
    "think": False,
    "stream": False,
    "options": {
        "num_predict": 64,
    },
}

request = Request(
    "http://localhost:11434/api/chat",
    data=json.dumps(payload).encode("utf-8"),
    headers={"Content-Type": "application/json"},
    method="POST",
)

start = perf_counter()

with urlopen(request, timeout=120) as response:
    result = json.load(response)

elapsed = perf_counter() - start

print("\n--- Resultado sem instruções ---")
print("Resposta:", result["message"]["content"])
print("Motivo:", result.get("done_reason"))
print(f"Tempo total: {elapsed:.2f}s")
print(f"Tokens de entrada: {result.get('prompt_eval_count')}")
print(
    f"Tempo de avaliação: "
    f"{result.get('prompt_eval_duration', 0) / 1e9:.2f}s"
)
print(f"Tokens de saída: {result.get('eval_count')}")
print(
    f"Tempo de geração: "
    f"{result.get('eval_duration', 0) / 1e9:.2f}s"
)
