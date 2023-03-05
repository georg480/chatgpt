import os
import unittest

from models.dateien import schreibe_protokol


class TestDateien(unittest.TestCase):
    def setUp(self):
        # Erstelle eine Testdatei
        self.testdatei = "testdatei.txt"
        with open(self.testdatei, "w", encoding="utf-8") as file:
            file.write("Dies ist eine Testdatei.")

    def tearDown(self):
        # Lösche die Testdatei nach dem Test
        os.remove(self.testdatei)

    def test_schreibe_protokol(self):
        # Teste, ob die Funktion den Inhalt in die Datei schreibt
        schreibe_protokol(self.testdatei, "Neuer Inhalt.")
        with open(self.testdatei, "r", encoding="utf-8") as file:
            inhalt = file.read()
        self.assertEqual(inhalt, "Dies ist eine Testdatei.Neuer Inhalt.")
