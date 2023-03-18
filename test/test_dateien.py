import os
import unittest

from models.dateien import lese_datei, schreibe_protokol


class TestDateien(unittest.TestCase):
    def test_schreibe_und_lese_protokol(self):
        datei_namen = "test_protokol.txt"
        inhalt_einfuegen = "Dies ist ein Test-Protokoll."
        schreibe_protokol(datei_namen, inhalt_einfuegen)
        self.assertTrue(os.path.exists(datei_namen))
        with open(datei_namen, "r", encoding="utf-8") as file:
            self.assertEqual(file.read(), inhalt_einfuegen)

        datei_inhalt = lese_datei(datei_namen)
        self.assertEqual(datei_inhalt, inhalt_einfuegen)
        os.remove(datei_namen)
