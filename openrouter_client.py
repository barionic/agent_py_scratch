import json
import os
from urllib.request import Request, urlopen

from llm_client import LLMClient


class OpenRouterClient:
    def __init__(self, model: str):
        self.model = model

    def chat(self, message: str) -> str:
        api_key = os.getenv("OPENROUTER_API_KEY")

        if not api_key:
            raise ValueError("A variável OPENROUTER_API_KEY não está configurada.")

        payload = {
            "model": self.model,
            "messages": [
                {"role": "user", "content": message}
            ],
            "stream": False,
            "max_tokens": 128
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

        with urlopen(request, timeout=60) as response:
            result = json.load(response)

        message_data = result["choices"][0]["message"]
        content = message_data.get("content")

        if not content:
            model_used = result.get("model", self.model)
            raise RuntimeError(f"O modelo '{model_used}' retornou uma resposta sem conteúdo textual.")

        return content

        
        #print(json.dumps(result, indent=2, ensure_ascii=False))
        #return result["choices"][0]["message"].get("content")