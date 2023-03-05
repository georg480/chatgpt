import unittest

from openai_com import chat


class TestChat(unittest.TestCase):
    def test_chat(self):
        anweisung = "Was ist die Hauptstadt von Frankreich?"
        antwort = chat(anweisung, "text-davinci-002")
        self.assertIsInstance(antwort, str)
        self.assertGreater(len(antwort), 0)
