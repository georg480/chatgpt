import os
import unittest

from models.dateien import schreibe_protokol


class TestDateien(unittest.TestCase):
    def setUp(self):
        self.testdatei = "testdatei.txt"
        with open(self.testdatei, "w", encoding="utf-8") as file:
            file.write("Dies ist eine Testdatei.")

    def tearDown(self):
        os.remove(self.testdatei)

    def test_schreibe_protokol(self):
        schreibe_protokol(self.testdatei, "Neuer Inhalt.")
        with open(self.testdatei, "r", encoding="utf-8") as file:
            inhalt = file.read()
        self.assertEqual(inhalt, "Dies ist eine Testdatei. Neuer Inhalt.")
