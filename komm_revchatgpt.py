import json
import os
from datetime import datetime

import openai
from revChatGPT.V1 import Chatbot

from models.dateien import schreibe_protokol
from models.functions import pruefe_py_gebaut

conf = json.load(open("chatgpt.json"))

convo_id = "46f4b87e-8fcd-43fc-9b8d-97845fdc7f74"
parent_id = "5d6b43fe-1042-428e-8614-4c476fd1c694"

chatbot = Chatbot(config=conf, conversation_id=convo_id, parent_id=parent_id)
# anweisung = input("Stellen Sie eine Frage: ") + ',"text-davinci-003", 4096'
# print(anweisung)
# antwort = list(chatbot.ask(anweisung))
# print(f"antwort liste:{antwort}")
# antwort = antwort[-1]['message']
# print(antwort)


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
#    id = antwort[-1]["id"]
 #   print(f"id: {id}")
#    gen_title = chatbot.gen_title(convo_id=convo_id, message_id="TEST Titel")
    #change_title= chatbot.change_title(convo_id=convo_id,title="Change")
    #delete_conversation= chatbot.delete_conversation(convo_id=convo_id)
    #print(f"delete_conversation: {delete_conversation}")
    #clear_conversations=chatbot.clear_conversations()
    #print(f"clear_conversations: {clear_conversations}")
    #reset_chat = chatbot.reset_chat()
    #print(f"reset_chat: {reset_chat}")
    #rollback_conversation = chatbot.rollback_conversation(num=1)
    #print(f"rollback_conversation: {rollback_conversation}")
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
