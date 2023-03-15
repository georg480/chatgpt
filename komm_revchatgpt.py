import json
import os
from datetime import datetime

import openai
from revChatGPT.V1 import Chatbot

from models.dateien import schreibe_protokol
from models.functions import pruefe_py_gebaut

conf = json.load(open("chatgpt.json"))

uuid = None

chatbot = Chatbot(config=conf, conversation_id=uuid, parent_id=uuid)
# anweisung = input("Stellen Sie eine Frage: ")
# antwort = list(chatbot.ask(anweisung))
# antwort = antwort[-1]['message']
# print(antwort)


def chat(anweisung, model, max_laenge):
    zeit_aktuell = datetime.now().strftime("%Y.%m.%d_%H:%M:%S")
    schreibe_protokol("protokoll.txt", f"zu gpt {zeit_aktuell}: {anweisung}\n")
    antwort = list(chatbot.ask(anweisung))
    antwort = antwort[-1]["message"]
    schreibe_protokol("protokoll.txt", f"von gpt {zeit_aktuell}: {antwort}\n")
    print(f"Antwort: {antwort}")
    return antwort


openai.api_key = os.getenv("OPENAI_API_KEY")


def erzeuge_unittest(skript_quelle: str, model):
    with open(skript_quelle, "r", encoding="utf-8") as file:
        datei_inhalt = file.readlines()
    funktion = "Schreibe zu der Funktion einen Unittest der in einem extra Datei ist."
    anweisung = f"{funktion}\n\n==== Python-Code ====\n\nPython-Code:\n{datei_inhalt}"
    print(f"anweisung gpt:{anweisung}")
    zeit_aktuell = datetime.now().strftime("%Y.%m.%d_%H:%M:%S")
    schreibe_protokol("protokoll.txt", f"zu gpt {zeit_aktuell}: {anweisung}\n")
    antwort = list(chatbot.ask(anweisung))
    antwort = antwort[-1]["message"]
    #    print(f"Antwort: {antwort}")
    schreibe_protokol("protokoll.txt", f"von gpt {zeit_aktuell}: {antwort}\n")
    print(f"Der geänderte Inhalt ist: {antwort}")
    try:
        with open("test/test_" + skript_quelle, "w", encoding="utf-8") as file:
            lines = antwort[antwort.index("imp") : -2]
            for line in lines.split("\\n', '"):
                print(line + "\n")
                file.write(line + "\n")
            print(f"Name des neuen Skripts: test_{skript_quelle}")
    except Exception as exc:
        print(f"Name des neuen Skripts: test_{skript_quelle}: {exc}")
        return
    pruefe_py_gebaut("test/test_" + skript_quelle)
    print(f"geänderte Funktion: {funktion}")
    print(f"prüfe in der test/test_{skript_quelle}")
