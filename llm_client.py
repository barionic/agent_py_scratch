from dataclasses import dataclass
from enum import Enum
from typing import Protocol

class FinishReason(Enum):
    COMPLETED = "completed"
    LENGTH_LIMIT = "length_limit"
    UNKNOWN = "unknown"
# FinishReason.LENGTH_LIMIT.value é "length_limit"

@dataclass
class GenerationResult:
    text: str
    finish_reason: FinishReason

class LLMClient(Protocol):
    def chat(self, message: str) -> GenerationResult:
        ...