import tempfile
import unittest
from pathlib import Path

from instruction_loader import load_instructions


class TestInstructionLoader(unittest.TestCase):

    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.instructions_dir = Path(self.temp_dir.name)

        (self.instructions_dir / "IDENTITY.md").write_text(
            "# Bimo\nSua identidade.",
            encoding="utf-8",
        )

        (self.instructions_dir / "SOUL.md").write_text(
            "# Soul\nSeu comportamento.",
            encoding="utf-8",
        )

    def tearDown(self):
        self.temp_dir.cleanup()

    def test_loads_instructions_as_system_messages(self):
        messages = load_instructions(self.instructions_dir)

        self.assertEqual(len(messages), 2)
        self.assertEqual(messages[0].role, "system")
        self.assertEqual(messages[1].role, "system")

    def test_loads_instructions_in_correct_order(self):
        messages = load_instructions(self.instructions_dir)

        self.assertIn("Sua identidade.", messages[0].content)
        self.assertIn("Seu comportamento.", messages[1].content)

    def test_raises_error_when_instruction_file_is_missing(self):
        (self.instructions_dir / "SOUL.md").unlink()

        with self.assertRaises(FileNotFoundError):
            load_instructions(self.instructions_dir)

    def test_raises_error_when_instruction_file_is_empty(self):
        (self.instructions_dir / "IDENTITY.md").write_text(
            "",
            encoding="utf-8",
        )

        with self.assertRaises(ValueError):
            load_instructions(self.instructions_dir)


if __name__ == "__main__":
    unittest.main()