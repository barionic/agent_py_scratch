import json
import os
from urllib.request import Request, urlopen

from llm_client import FinishReason, GenerationResult

class OllamaCloudClient:
    def __init__(self, model: str):
        self.model = model
        self.api_key = os.environ.get("OLLAMA_API_KEY")

        if not self.api_key:
            raise ValueError(
                "A variável de ambiente OLLAMA_API_KEY não foi configurada"
            )

    def chat(self, message: str) -> GenerationResult:
        payload = {
            "model": self.model,
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
            "https://ollama.com/api/chat",
            data=json.dumps(payload).encode("utf-8"),
            headers={
                "Content-Type": "application/json",
                "Authorization": f"Bearer {self.api_key}",
            },
            method="POST",
        )

        with urlopen(request, timeout=60) as response:
            result = json.load(response)

        done_reason = result.get("done_reason")

        #print("Motivo do encerramento: ", done_reason)
        #print("Tokens gerados: ", result.get("eval_count"))

        if done_reason == "stop":
            finish_reason = FinishReason.COMPLETED
        elif done_reason == "length":
            finish_reason = FinishReason.LENGTH_LIMIT
        else:
            finish_reason = FinishReason.UNKNOWN

        return GenerationResult(
            text=result["message"]["content"],
            finish_reason=finish_reason
        )

# Test to run in terminal: LLM_PROVIDER=ollama-cloud LLM_MODEL="beam" python main.py