import os
import unittest
from unittest.mock import patch

from gpt3 import gpt3


class TestGpt3(unittest.TestCase):
    @patch("models.gpt3.openai.Completion.create")
    @patch("models.gpt3.os.getenv")
    def test_gpt3(self, mock_getenv, mock_completion_create):
        mock_getenv.return_value = os.getenv("OPENAI_API_KEY")
        mock_response = {
            "choices": [{"text": "This is a test response."}],
        }
        mock_completion_create.return_value = mock_response

        prompt = "This is a test prompt."
        expected_answer = "This is a test response."
        expected_new_prompt = prompt + expected_answer

        answer, new_prompt = gpt3(prompt)

        mock_getenv.assert_called_with("OPENAI_API_KEY")
        mock_completion_create.assert_called_with(
            prompt=prompt,
            engine="text-davinci-003",
            max_tokens=512,
            temperature=0.7,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0,
            stop=[],
        )

        self.assertEqual(answer, expected_answer)
        self.assertEqual(new_prompt, expected_new_prompt)
