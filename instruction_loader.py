from pathlib import Path

from llm_client import ChatMessage

def load_instructions(
    instructions_dir: Path | None = None,
) -> list[ChatMessage]:

    if instructions_dir is None:
        instructions_dir = Path(__file__).resolve().parent / "instructions"

    instructions_files = [
        "IDENTITY.md",
        "SOUL.md" 
    ]

    messages = []

    for filename in instructions_files:
        file_path = instructions_dir / filename

        if not file_path.is_file():
            raise FileNotFoundError(f"Arquivo de instrução não encontrado: {file_path}")

        content = file_path.read_text(encoding="utf-8").strip()

        if not content:
            raise ValueError(f"Arquivo de instrução está vazio: {file_path}")

        messages.append(
            ChatMessage(
                role="system",
                content=content
            )
        )

    return messages