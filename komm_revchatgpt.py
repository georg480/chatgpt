import glob
import json
import os
from datetime import datetime

import openai
from revChatGPT.V1 import Chatbot, logger

from models.dateien import (
    aendere_datei_pfard,
    gebe_nur_dateinamen,
    lese_datei,
    lese_gesuchte_dateinamen,
    schreibe_datei,
    schreibe_md,
    schreibe_protokol,
)
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


def erzeuge_unittest(skript_quelle: str):
    print(f"skript_quelle else: {skript_quelle}")
    datei_inhalt = lese_datei(skript_quelle + ".py")
    anweisung = (
        f"Schreibe zu der Funktion einen Unittest der in einem extra Datei ist.\n"
        f"Dateiname: {skript_quelle}.py\nPython-Code:\n{datei_inhalt}"
    )
    antwort = chat_gpt_chat(anweisung)
    skript_quelle = gebe_nur_dateinamen(skript_quelle)
    if not "```" in antwort:
        print(f"\nkeine ``` in Antwort von {skript_quelle}\n")
        breakpoint
    else:
        antwort = antwort[antwort.index("import ") : antwort.rindex("if __") - 1]
        schreibe_datei(f"test/test_{skript_quelle}.py", antwort)
        pruefe_py_gebaut(f"test/test_{skript_quelle}.py")
        print(f"prüfe in der test/test_{skript_quelle}.py")


def erzeuge_uml():
    for skript_quelle in lese_gesuchte_dateinamen("**/*.py"):
        skript_quelle = aendere_datei_pfard(skript_quelle)[:-3]
        if skript_quelle[-8:] == "__init__":
            print(f"__init__: {skript_quelle}")
            breakpoint
        else:
            print(f"skript_quelle else: {skript_quelle}")
            datei_inhalt = lese_datei(skript_quelle + ".py")
            anweisung = (
                f"Kannst du ein UML Klassendiagramm{FUNKTION_STANDART}\n"
                f"Dateiname: {skript_quelle}.py\nPython-Code:\n{datei_inhalt}"
            )
            antwort = chat_gpt_chat(anweisung)
            if not "```" in antwort:
                print(f"\nkeine ``` in Antwort von {skript_quelle}\n")
                breakpoint
            else:
                skript_quelle = gebe_nur_dateinamen(skript_quelle)
                schreibe_md(f"uml/{skript_quelle}_klassen_diagramm.md", antwort)
                anweisung = (
                    f"Kannst du ein UML Sequenzdiagramm{FUNKTION_STANDART}\n"
                    f"Dateiname: {skript_quelle}.py\nPython-Code:\n{datei_inhalt}"
                )
                antwort = chat_gpt_chat(anweisung)
                if not "```" in antwort:
                    print(f"\nkeine ``` in Antwort von {skript_quelle}\n")
                    breakpoint
                else:
                    skript_quelle = gebe_nur_dateinamen(skript_quelle)
                    schreibe_md(f"uml/{skript_quelle}_sequenz_diagramm.md", antwort)
