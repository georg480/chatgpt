import os
import tempfile
import unittest

from models.dateien import lese_datei, schreibe_datei, schreibe_protokol


class TestDateien(unittest.TestCase):
    def setUp(self):
        self.test_dir = tempfile.mkdtemp()
        self.test_file = os.path.join(self.test_dir, "test.txt")

    def tearDown(self):
        os.remove(self.test_file)
        os.rmdir(self.test_dir)

    def test_schreibe_protokol(self):
        schreibe_protokol(self.test_file, "Test Protokoll")
        with open(self.test_file, "r") as file:
            content = file.read()
            self.assertEqual(content, "Test Protokoll")

    def test_lese_datei(self):
        with open(self.test_file, "w") as file:
            file.write("Testinhalt\nzweite Zeile")
        content = lese_datei(self.test_file)
        self.assertEqual(content, "Testinhalt zweite Zeile")

    def test_schreibe_datei(self):
        schreibe_datei(self.test_file, "Testinhalt")
        with open(self.test_file, "r") as f:
            content = f.read()
            self.assertEqual(content, "Testinhalt")
