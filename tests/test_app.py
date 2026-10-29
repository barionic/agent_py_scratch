import unittest
from contextlib import redirect_stdout
from io import StringIO
from unittest.mock import patch

from app import main
from fake_llm_client import FakeLLMClient
from llm_client import ChatMessage, FinishReason


class TestApp(unittest.TestCase):
    def run_app(self, client, user_inputs):
        output = StringIO()

        with patch("builtins.input", side_effect=user_inputs):
            with redirect_stdout(output):
                main(client)

        return output.getvalue()

    def test_completed_shows_answer_without_warning(self):
        client = FakeLLMClient()
        output = self.run_app(client, ["Teste", "/sair"])

        self.assertIn("Resposta simulada para: Teste", output)
        self.assertNotIn("[AVISO]", output)

    def test_length_limit_shows_answer_and_warning(self):
        client = FakeLLMClient(FinishReason.LENGTH_LIMIT)
        output = self.run_app(client, ["Teste", "/sair"])

        self.assertIn("Resposta simulada para: Teste", output)
        self.assertIn("pode estar incompleta", output)

    def test_unknown_shows_answer_and_warning(self):
        client = FakeLLMClient(FinishReason.UNKNOWN)
        output = self.run_app(client, ["Teste", "/sair"])

        self.assertIn("Resposta simulada para: Teste", output)
        self.assertIn("Não foi possível determinar", output)

    def test_history_is_sent_on_following_turn(self):
        client = FakeLLMClient()

        self.run_app(
            client,
            ["Meu nome é Buzz", "Qual é meu nome?", "/sair"],
        )

        self.assertEqual(len(client.received_histories), 2)

        second_history = client.received_histories[1]

        self.assertEqual(
            second_history,
            [
                ChatMessage(
                    role="user",
                    content="Meu nome é Buzz",
                ),
                ChatMessage(
                    role="assistant",
                    content="Resposta simulada para: Meu nome é Buzz",
                ),
                ChatMessage(
                    role="user",
                    content="Qual é meu nome?",
                ),
            ],
        )

    def test_exit_does_not_call_client(self):
        client = FakeLLMClient()

        self.run_app(client, ["/sair"])

        self.assertEqual(client.received_histories, [])

    def test_blank_input_is_ignored(self):
        client = FakeLLMClient()
    
        self.run_app(client, ["   ", "Oi", "/sair"])
    
        self.assertEqual(len(client.received_histories), 1)


if __name__ == "__main__":
    unittest.main()

# Test to run in terminal: python -m unittest discover -s tests -v