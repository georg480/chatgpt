import unittest

from komm_chat import komm_chat
from openai_com import erzeuge_unittest


class TestSkript(unittest.TestCase):
    def test_erzeuge_unittest(self):
        skripname = "test_skript"
        model = "text-davinci-003"
        self.assertEqual(erzeuge_unittest(skripname, model), "Skript erfolgreich getestet")

    def test_komm_chat(self):
        self.assertEqual(komm_chat(), "Chat erfolgreich beendet")

if __name__ == '__main__':
  unittest.main()
  '\n