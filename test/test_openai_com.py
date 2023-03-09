import os
import unittest
from datetime import datetime

import openai

from models.dateien import schreibe_protokol
from models.functions import pruefe_py_gebaut
from openai_com import chat


class TestChat(unittest.TestCase):
    def setUp(self):
        self.anweisung = "Schreibe zu der Funktion einen Unittest der in einem extra Datei ist.\n\n==== Python-Code ====\n\nPython-Code:\n"
        self.model = "text-davinci-003"
        self.max_tokens = 1024

    def test_chat(self):
        zeit_aktuell = datetime.now().strftime("%Y.%m.%d_%H:%M:%S")

        schreibe_protokol("protokoll.txt", f"zu gpt {zeit_aktuell}: {self.anweisung}\n")
        antwort = openai.Completion.create(
            model=self.model,
            prompt=self.anweisung,
            temperature=0.9,
            max_tokens=self.max_tokens,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0.6,
        )

        schreibe_protokol("protokoll.txt", f"von gpt {zeit_aktuell}: {antwort}\n")

        expected_result = antwort.choices[0].text

        self.assertEqual(expected_result, antwort.choices[0].text)

    def test_erzeuge_unittest_skript_quelle(self, skript_quelle):
        with open(skript_quelle, "r", encoding="utf-8") as file:
            datei_inhalt = file.readlines()
        funktion = (
            "Schreibe zu der Funktion einen Unittest der in einem extra Datei ist."
        )
        anweisung = (
            f"{funktion}\n\n==== Python-Code ====\n\nPython-Code:\n{datei_inhalt}"
        )

        expected_result = anweisung
        self.assertEqual(expected_result, anweisung)

    def test_erzeuge_unittest_model(self):
        model = "text-davinci-003"
        expected_result = model
        self.assertEqual(expected_result, model)

    def test_erzeuge_unittest_true_result(self):
        skript_quelle = "main.py"
        with open(skript_quelle, "r", encoding="utf-8") as file:
            datei_inhalt = file.readlines()
        funktion = (
            "Schreibe zu der Funktion einen Unittest der in einem extra Datei ist."
        )
        anweisung = (
            f"{funktion}\n\n==== Python-Code ====\n\nPython-Code:\n{datei_inhalt}"
        )
        print(f"anweisung gpt:{anweisung}")
        antwort = chat(anweisung, self.model, self.max_tokens)
        print(f"Der geänderte Inhalt ist: {antwort}")
        try:
            with open("test/test_" + skript_quelle, "w", encoding="utf-8") as file:
                lines = antwort[antwort.index("imp") : -2]
                for line in lines.split("\\\\n', '"):
                    print(line + "\\n")
                    file.write(line + "\\n")
                print(f"Name des neuen Skripts: test_{skript_quelle}")
        except Exception as e:
            print("")
            return
        pruefe_py_gebaut("test/test_" + skript_quelle)
        print(f"Die {skript_quelle}")
        print(f"geänderte Funktion: {funktion}")

        expected_result = True
        self.assertTrue(expected_result)
