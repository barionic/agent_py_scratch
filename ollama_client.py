import json
from urllib.request import Request, urlopen

from llm_client import ChatMessage, FinishReason, GenerationResult

class OllamaClient:
    def __init__(self, model: str):
        self.model = model

    def chat(self, messages: list[ChatMessage]) -> GenerationResult:
        payload = {
            "model": self.model,
            "messages": [
                {
                    "role": message.role,
                    "content": message.content,
                }
                for message in messages
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

        done_reason = result.get("done_reason")

        if done_reason == "stop":
            finish_reason = FinishReason.COMPLETED
        elif done_reason == "length":
            finish_reason = FinishReason.LENGTH_LIMIT
        else:
            finish_reason = FinishReason.UNKNOWN

        return GenerationResult(
            text=result["message"]["content"],
            finish_reason=finish_reason,
        )