import json
from datetime import datetime

from revChatGPT.V1 import Chatbot

from models.dateien import schreibe_protokol

conf = json.load(open("chatgpt.json"))
conf["model"] = "text-davinci-003"

chatbot = Chatbot(conf, conversation_id=None, parent_id=None)
# anweisung = input("Stellen Sie eine Frage: ")
# antwort = list(chatbot.ask(anweisung))
# sorted_messages = sorted([x['text'] if 'text' in x else x['message'] for x in antwort], key=lambda x: len(x))
# print(sorted_messages[-1])


def chat(anweisung, model, max_laenge):
    zeit_aktuell = datetime.now().strftime("%Y.%m.%d_%H:%M:%S")
    schreibe_protokol("protokoll.txt", f"zu gpt {zeit_aktuell}: {anweisung}\n")
    antwort = list(chatbot.ask(anweisung))
    sorted_messages = sorted(
        [x["text"] if "text" in x else x["message"] for x in antwort],
        key=lambda x: len(x),
    )
    schreibe_protokol("protokoll.txt", f"von gpt {zeit_aktuell}: {antwort}\n")
    print(f"Antwort: {sorted_messages[-1]}")
    return sorted_messages[-1]
