import unittest

from komm_chat import komm_chat
from models.dateien import lese_datei, schreibe_datei
from openai_com import chat, erzeuge_unittest


class TestOpenAIFunktionen(unittest.TestCase):
    def test_komm_chat(self):
        self.assertIsNotNone(komm_chat())

    def test_lese_datei(self):
        englischDatei = lese_datei("englischer_text.txt")
        self.assertIsNotNone(englischDatei)

    def test_schreibe_datei(self):
        deutschDatei = schreibe_datei("deutscher_text.txt", "Hallo Welt")
        self.assertIsNotNone(deutschDatei)

    def test_chat(self):
        anweisung = "Hallo Welt"
        antwort = chat(anweisung, "text-davinci-003", 2150)
        self.assertIsNotNone(antwort)

    def test_erzeuge_unittest(self):
        unittestSkript = erzeuge_unittest(
            "test_openai_funktionen.py", "text-davinci-003"
        )
        self.assertIsNotNone(unittestSkript)


if __name__ == "__main__":
    unittest.main
