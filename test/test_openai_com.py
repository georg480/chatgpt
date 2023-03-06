import unittest

from models.dateien import schreibe_protokol
from models.functions import pruefe_py_gebaut


class TestChat(unittest.TestCase):
    def test_chat_funktion(self):
        model = "gpt-2"
        max_tokens = 1024
        anweisung = (
            "Schreibe zu der Funktion einen Unittest der in einem extra Datei ist."
        )
        antwort = chat(anweisung, model, max_tokens)
        expected_str = "import unittest\nfrom models.dateien import schreibe_protokol\nfrom models.functions import pruefe_py_gebaut\n\nclass TestChat(unittest.TestCase):\n\n    def test_chat_funktion(self):"
        self.assertIn(expected_str, antwort)


if __name__ == "__main__":
    unittest.main
