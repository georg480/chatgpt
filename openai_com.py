import os
from datetime import datetime

import openai

from models.dateien import schreibe_protokol
from models.functions import pruefe_py_gebaut

openai.api_key = os.getenv("OPENAI_API_KEY")

# from transformers import AutoTokenizer
# gpt2_tokenizer = AutoTokenizer.from_pretrained("gpt2", use_fast=True)
#
# text_in = "bla bla"
# tokens = gpt2_tokenizer.tokenize(text_in)


def chat(anweisung, model):
    zeit_aktuell = datetime.now().strftime("%Y.%m.%d_%H:%M:%S")
    schreibe_protokol("protokoll.txt", f"zu gpt {zeit_aktuell}: {anweisung}\n")
    antwort = openai.Completion.create(
        model=model,
        prompt=anweisung,
        temperature=0.9,
        max_tokens=2150,  #  max_tokens,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0.6,
    )
    schreibe_protokol("protokoll.txt", f"von gpt {zeit_aktuell}: {antwort}\n")
    print(f"Antwort: {antwort.choices[0].text}")
    return antwort.choices[0].text


def erzeuge_unittest(skript_quelle: str, model):
    with open(skript_quelle, "r", encoding="utf-8") as file:
        datei_inhalt = file.readlines()
    funktion = "Schreibe zu der Funktion einen Unittest der in einem extra Datei ist."
    anweisung = f"{funktion}\n\n==== Python-Code ====\n\nPython-Code:\n{datei_inhalt}"
    print(f"anweisung gpt:{anweisung}")
    antwort = chat(anweisung, model)
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
