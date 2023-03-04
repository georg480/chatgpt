import unittest
from datetime import datetime

from models.dateien import schreibe_protokol
from openai_com import chat


class TestOpenAIChat(unittest.TestCase):
    def test_chat(self):
        model = "text-davinci-003"
        anweisung = "Gebe Hallo Georg aus."
        zeit_aktuell = datetime.now().strftime("%Y.%m.%d_%H:%M:%S")
        schreibe_protokol("Protokoll.txt", f"zu gpt {zeit_aktuell}: {anweisung}\n")
        antwort = chat(anweisung, model)
        schreibe_protokol("Protokoll.txt", f"von gpt {zeit_aktuell}: {antwort}\n")

        # Überprüfe, ob eine Antwort zurückgegeben wurde
        self.assertIsNotNone(antwort)

        while True:
            benutzer_eingabe = input("Frage /Eingabe ein. a(aus), u (Eng->D)")

            if benutzer_eingabe.lower() == "a":
                break
            elif benutzer_eingabe.lower() == "u":
                benutzer_eingabe = input("Englischer Text")
                anweisung = f"Translate this into German:\n\n{benutzer_eingabe}\n\n1."
                schreibe_protokol(
                    "Protokoll.txt", f"zu gpt {zeit_aktuell}: {anweisung}\n"
                )
                antwort = chat(anweisung, model)
                schreibe_protokol(
                    "Protokoll.txt", f"von gpt {zeit_aktuell}: {antwort}\n"
                )
                print("Protokoll.txt", f"von gpt {zeit_aktuell}: {antwort}\n")

        # Überprüfe, ob eine Antwort zurückgegeben wurde
        self.assertIsNotNone(antwort)
