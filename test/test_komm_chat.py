import unittest
from io import StringIO
from unittest.mock import patch

from komm_chat import komm_chat


class TestKommChat(unittest.TestCase):
    def test_chat(self):
        test_input = ["Hallo", "Kannst du mir das Wetter sagen?", "Auf Wiedersehen"]
        expected_output = [
            "GPT-3:Guten Tag, wie kann ich Ihnen helfen?",
            "GPT-3:Ja, in welcher Stadt möchten Sie das Wetter wissen?",
            "GPT-3:Das Wetter in Berlin ist sonnig bei einer Temperatur von 22 Grad Celsius.",
            "GPT-3:Gibt es noch etwas, bei dem ich helfen kann?",
            "GPT-3:Auf Wiedersehen!",
        ]
        with patch("sys.stdout", new=StringIO()) as fake_output:
            with patch("builtins.input", side_effect=test_input):
                komm_chat()
        actual_output = fake_output.getvalue().strip().split("\n")
        self.assertEqual(actual_output, expected_output)
