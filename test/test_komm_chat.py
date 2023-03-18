import unittest
from unittest.mock import patch

from komm_chat import komm_chat


class TestKommChat(unittest.TestCase):
    def test_komm_chat(self):
        # Test a simple exchange between human and AI.
        with patch(
            "builtins.input",
            side_effect=["Was ist das Wetter heute?", "Was ist deine Lieblingsfarbe?"],
        ):
            with patch("builtins.print") as mock_print:
                komm_chat()

        mock_print.assert_any_call("GPT-3:Das Wetter heute ist sonnig.")
        mock_print.assert_any_call("GPT-3:Meine Lieblingsfarbe ist Blau.")
