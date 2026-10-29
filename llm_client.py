from dataclasses import dataclass
from enum import Enum
from typing import Literal, Protocol

class FinishReason(Enum):
    COMPLETED = "completed"
    LENGTH_LIMIT = "length_limit"
    UNKNOWN = "unknown"
# FinishReason.LENGTH_LIMIT.value é "length_limit"

MessageRole = Literal["system", "user", "assistant"]

@dataclass(frozen=True)
class ChatMessage:
    role: MessageRole
    content: str

@dataclass
class GenerationResult:
    text: str
    finish_reason: FinishReason

class LLMClient(Protocol):
    def chat(self, message: list[ChatMessage]) -> GenerationResult:
        ...