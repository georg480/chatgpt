import unittest
from unittest.mock import MagicMock, patch

from komm_revchatgpt import chat_gpt_chat


class TestChatGPT(unittest.TestCase):
    @patch("revChatGPT.Chatbot")
    def test_chat_gpt_chat(self, mock_chatbot):
        mock_chatbot_instance = MagicMock()
        mock_chatbot.return_value = mock_chatbot_instance
        mock_response = {"message": "Hello, World!"}
        mock_chatbot_instance.ask.return_value = [mock_response]
        result = chat_gpt_chat("Hello, GPT!")
        self.assertEqual(result, "Hello, World!")
        mock_chatbot.assert_called_once_with(
            config={"engine": "text-davinci-002"},
            conversation_id="339e6ebd-e5f0-49f0-b54a-05f9614125b1",
            parent_id="a0c3abd8-b9bd-4b60-b31a-d73abf0ae7b7",
        )
        mock_chatbot_instance.ask.assert_called_once_with(
            "Hello, GPT!",
            conversation_id="339e6ebd-e5f0-49f0-b54a-05f9614125b1",
            parent_id="a0c3abd8-b9bd-4b60-b31a-d73abf0ae7b7",
        )
