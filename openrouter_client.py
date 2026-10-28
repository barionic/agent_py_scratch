import json
import os
from urllib.request import Request, urlopen
from urllib.error import HTTPError

from llm_client import FinishReason, GenerationResult


class OpenRouterClient:
    def __init__(self, model: str):
        self.model = model

    def chat(self, message: str) -> GenerationResult:
        api_key = os.getenv("OPENROUTER_API_KEY")

        if not api_key:
            raise ValueError("A variável OPENROUTER_API_KEY não está configurada.")

        payload = {
            "model": self.model,
            "messages": [
                {"role": "user", "content": message}
            ],
            "stream": False,
            "max_tokens": 1024
        }

        request = Request(
            "https://openrouter.ai/api/v1/chat/completions",
            data=json.dumps(payload).encode("utf-8"),
            headers={
                "Authorization": f"Bearer {api_key}",
                "Content-Type": "application/json",
            },
            method="POST",
        )

        try:
            with urlopen(request, timeout=60) as response:
                result = json.load(response)
        except HTTPError as error:
            #print("Status HTTP:", error.code)
            #print(error.read().decode("utf-8", errors="replace"))
            raise

        message_data = result["choices"][0]["message"]
        content = message_data.get("content")

        if not content:
            model_used = result.get("model", self.model)
            raise RuntimeError(f"O modelo '{model_used}' retornou uma resposta sem conteúdo textual.")

        api_reason = result["choices"][0].get("finish_reason")

        if api_reason == "stop":
            finish_reason = FinishReason.COMPLETED
        elif api_reason == "length":
            finish_reason = FinishReason.LENGTH_LIMIT
        else:
            finish_reason = FinishReason.UNKNOWN

        return GenerationResult(
            text=content,
            finish_reason = finish_reason
        )

# Test to run in terminal: LLM_PROVIDER=openrouter LLM_MODEL=nvidia/nemotron-3-ultra-550b-a55b:free python main.py