import io
import unittest
from unittest.mock import patch

from main import komm_chat


class TestKommChat(unittest.TestCase):
    @patch("builtins.input", side_effect=["Hallo", "Tschüss"])
    def test_komm_chat(self, mock_input):
        with patch("sys.stdout", new=io.StringIO()) as mock_output:
            komm_chat()
            self.assertIn("Bot:", mock_output.getvalue())
