import unittest

from models.dateien import lese_datei, schreibe_datei
from openai_com import chat, erzeuge_unittest


class TestOpenAiCom(unittest.TestCase):
    
    def setUp(self):
        self.model = "text-davinci-003"
    
    def test_chat(self):
        anweisung = "Wie ist das Wetter heute?"
        antwort = chat(anweisung, self.model, 150)
        self.assertIsNotNone(antwort)

    def test_lese_schreibe_datei(self):
        englischer_text = "Hello World"
        schreibe_datei("englischer_text.txt", englischer_text)
        antwort_lesen = lese_datei("englischer_text.txt")
        self.assertEqual(englischer_text, antwort_lesen)
