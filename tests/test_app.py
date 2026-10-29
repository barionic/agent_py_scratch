import unittest
from contextlib import redirect_stdout
from io import StringIO
from unittest.mock import patch

from app import main
from fake_llm_client import FakeLLMClient
from llm_client import FinishReason


class TestApp(unittest.TestCase):
    def run_app(self, client):
        output = StringIO()

        with patch("builtins.input", return_value="Teste"):
            with redirect_stdout(output):
                main(client)

        return output.getvalue()

    def test_completed_shows_answer_without_warning(self):
        client = FakeLLMClient()
        output = self.run_app(client)

        self.assertIn("Resposta simulada para: Teste", output)
        self.assertNotIn("[AVISO]", output)

    def test_length_limit_shows_answer_and_warning(self):
        client = FakeLLMClient(FinishReason.LENGTH_LIMIT)
        output = self.run_app(client)

        self.assertIn("Resposta simulada para: Teste", output)
        self.assertIn("pode estar incompleta", output)

    def test_unknown_shows_answer_and_warning(self):
        client = FakeLLMClient(FinishReason.UNKNOWN)
        output = self.run_app(client)

        self.assertIn("Resposta simulada para: Teste", output)
        self.assertIn("Não foi possível determinar", output)


if __name__ == "__main__":
    unittest.main()