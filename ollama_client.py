import json
from urllib.request import Request, urlopen


def chat(message: str) -> str:
    payload = {
        "model": "qwen3.5:0.8b",
        "messages": [
            {"role": "user", "content": message}
        ],
        "think": False,
        "stream": False,
        "options": {
            "num_predict": 128
        },
    }

    request = Request(
        "http://localhost:11434/api/chat",
        data=json.dumps(payload).encode("utf-8"),
        headers={"Content-Type": "application/json"},
        method="POST",
    )

    with urlopen(request, timeout=60) as response:
        result = json.load(response)

    return result["message"]["content"]


