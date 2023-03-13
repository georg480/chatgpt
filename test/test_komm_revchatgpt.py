import unittest
from unittest.mock import patch

from komm_revchatgpt import chat


class TestChatbot(unittest.TestCase):
    def test_chat(self):
        with patch("builtins.input", return_value="Wie geht es dir?"):
            response = chat("Wie geht es dir?", "text-davinci-003", 100)
        self.assertIsInstance(response, str)
        self.assertGreater(len(response), 0)
