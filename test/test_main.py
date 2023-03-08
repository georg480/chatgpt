import unittest

from komm_chat import komm_chat
from openai_com import chat, erzeuge_unittest


class TestKommChat(unittest.TestCase):
    def setUp(self):
        self.MODEL = "text-davinci-003"

    def test_chat(self):
        anweisung = "Translate this into German: This is a test"
        antwort = chat(anweisung, self.MODEL, 150)
        self.assertEqual(antwort, "Dies ist ein Test")

    def test_komm_chat(self):
        eingabe_benutzer = "c"
        self.assertTrue(komm_chat())

    def test_erzeuge_unittest(self):
        skriptname = "komm_chat"
        self.assertTrue(erzeuge_unittest(skriptname, self.MODEL))


if __name__ == "__main__":
    unittest.main
