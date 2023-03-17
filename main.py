import os

from komm_chat import komm_chat
from komm_revchatgpt import chat_gpt_chat, erzeuge_uml, erzeuge_unittest
from models.dateien import lese_datei, schreibe_datei
from models.functions import pruefe_py_gebaut

MODEL = "davinci"

while True:
    eingabe_benutzer = input(
        "Eingabe a(abl), e(erkl.Code), f(Frage), p(prü), t(Unittest), u(E->D), x"
    )
    if eingabe_benutzer.lower() == "u":
        print(lese_datei("englischer_text.txt"))
        ANWEISUNG = (
            "Translate this into German:\n\n"
            + lese_datei("englischer_text.txt")
            + "\n\n"
        )
        ANTWORT = chat_gpt_chat(ANWEISUNG)
        print(f"\n{ANTWORT}")
        schreibe_datei("deutscher_text.txt", ANTWORT)
    elif eingabe_benutzer.lower() == "a":
        erzeuge_uml()
    elif eingabe_benutzer.lower() == "c":
        komm_chat()
    elif eingabe_benutzer.lower() == "t":
        erzeuge_unittest(input("Skript Name?"), MODEL)
    elif eingabe_benutzer.lower() == "p":
        pruefe_py_gebaut(input("Skript Name?"))
    elif eingabe_benutzer.lower() == "f":
        ANWEISUNG = input("Eingabe Frage")
        ANTWORT = chat_gpt_chat(ANWEISUNG)
    elif eingabe_benutzer.lower() == "e":
        ANWEISUNG = input("Welche Datei")
        ANWEISUNG = (
            "Kannst du erklären, was der Code macht und das Ergebnis als Markdown ausgeben?\n"
            + lese_datei(ANWEISUNG)
        )
        print(ANWEISUNG)
        ANTWORT = chat_gpt_chat(ANWEISUNG)
    elif eingabe_benutzer.lower() == "x":
        break
    else:
        print(eingabe_benutzer)
