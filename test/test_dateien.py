import os
import unittest

from models.dateien import schreibe_protokol


class TestDateien(unittest.TestCase):
    def setUp(self):
        self.datei_name = "test_protokoll.txt"
        self.inhalt = "Testinhalt"

    def tearDown(self):
        os.remove(self.datei_name)

    def test_schreibe_protokol(self):
        schreibe_protokol(self.datei_name, self.inhalt)
        with open(self.datei_name, "r", encoding="utf-8") as file:
            gelesener_inhalt = file.read()
        self.assertEqual(gelesener_inhalt, self.inhalt)
