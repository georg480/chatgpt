import glob
import json
import os
from datetime import datetime

import openai
from revChatGPT.V1 import Chatbot, logger

from models.dateien import lese_datei, schreibe_datei, schreibe_protokol, lese_gesuchte_dateinamen, aendere_datei_pfard, gebe_nur_dateinamen, schreibe_md
from models.functions import pruefe_py_gebaut

conf = json.load(open("chatgpt.json"))

FUNKTION_STANDART = " erstellen und das Ergebnis als Markdown ausgeben?"
convo_id = "339e6ebd-e5f0-49f0-b54a-05f9614125b1"
parent_id = "a0c3abd8-b9bd-4b60-b31a-d73abf0ae7b7"

chatbot = Chatbot(config=conf, conversation_id=convo_id, parent_id=parent_id)


def chat_gpt_chat(anweisung):
    zeit_aktuell = datetime.now().strftime("%Y.%m.%d_%H:%M:%S")
    print(f"zu gpt: \n{anweisung}")
    schreibe_protokol("protokoll.txt", f"zu gpt {zeit_aktuell}: {anweisung}\n")
    try:
        for antwort in chatbot.ask(
            anweisung,
            conversation_id=chatbot.config.get("conversation"),
            parent_id=chatbot.config.get("parent_id"),
        ):
            pass
        antwort = antwort["message"]
        print(f"antwort von gpt: \n{antwort}")
        schreibe_protokol("protokoll.txt", f"von gpt {zeit_aktuell}: {antwort}\n")
        return antwort
    except Exception as e:
        logger.exception(e)
        print(e)


def chat(anweisung, model, max_laenge):
    zeit_aktuell = datetime.now().strftime("%Y.%m.%d_%H:%M:%S")
    schreibe_protokol("protokoll.txt", f"zu gpt {zeit_aktuell}: {anweisung}\n")
    antwort = list(chatbot.ask(anweisung))
    get_conversations = chatbot.get_conversations(offset=0, limit=20, encoding=None)
    print(get_conversations)
    convo_id = antwort[-1]["conversation_id"]
    print(f"convo_id: {convo_id}")
    parent_id = antwort[-1]["parent_id"]
    print(f"parent_id: {parent_id}")
    get_msg_history = chatbot.get_msg_history(convo_id=convo_id, encoding=None)
    print(get_msg_history)
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


def erzeuge_uml():
    for skript_quelle in lese_gesuchte_dateinamen("**/*.py"):
        skript_quelle = aendere_datei_pfard(skript_quelle)[:-3]
        if skript_quelle[-8:] == "__init__":
            print(f"__init__: {skript_quelle}")
            breakpoint
        else:
            print(f"skript_quelle else: {skript_quelle}")
            datei_inhalt = lese_datei(skript_quelle + ".py")
            anweisung = f"Kannst du ein UML Klassendiagramm{FUNKTION_STANDART}\n" \
                        f"Dateiname: {skript_quelle}.py\nPython-Code:\n{datei_inhalt}"
            antwort = chat_gpt_chat(anweisung)
            if not "```" in antwort:
                print(f"\nkeine ``` in Antwort von {skript_quelle}\n")
                breakpoint
            else:
                skript_quelle = gebe_nur_dateinamen(skript_quelle)
                schreibe_md(f"uml/{skript_quelle}_klassen_diagramm.md", antwort)
                anweisung = f"Kannst du ein UML Sequenzdiagramm{FUNKTION_STANDART}\n" \
                            f"Dateiname: {skript_quelle}.py\nPython-Code:\n{datei_inhalt}"
                antwort = chat_gpt_chat(anweisung)
                if not "```" in antwort:
                    print(f"\nkeine ``` in Antwort von {skript_quelle}\n")
                    breakpoint
                else:
                    skript_quelle = gebe_nur_dateinamen(skript_quelle)
                    schreibe_md(f"uml/{skript_quelle}_sequenz_diagramm.md", antwort)
