import os

from komm_chat import komm_chat
from komm_github import git_commit, git_push
from komm_revchatgpt import chat_gpt_chat, erzeuge_uml, erzeuge_unittest
from models.dateien import lese_datei, schreibe_datei
from models.functions import eingabe, pruefe_py_gebaut, sprechen, aufnahme


MODEL = "davinci"

while True:
    eingabe_benutzer = eingabe(
        "Eingabe a(abl), c(com), e(erkl.Code), f(Frage), p(prü), pu(push), t(Unittest.md), u(E->D), x"
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
        git_commit()
    elif eingabe_benutzer.lower() == "t":
        erzeuge_unittest(eingabe("Skript Name?")[:-3])
    elif eingabe_benutzer.lower() == "p":
        pruefe_py_gebaut(eingabe("Skript Name?"))
    elif eingabe_benutzer.lower() == "pu":
        git_push()
    elif eingabe_benutzer.lower() == "f":
        ANWEISUNG = aufnahme()
        ANTWORT = chat_gpt_chat(ANWEISUNG)
        sprechen(ANTWORT)
    elif eingabe_benutzer.lower() == "e":
        ANWEISUNG = eingabe("Welche Datei")
        ANWEISUNG = (
            "Kannst du erkläre"
            "n, was der Code macht und das Ergebnis als Markdown ausgeben?\n"
            + lese_datei(ANWEISUNG)
        )
        print(ANWEISUNG)
        ANTWORT = chat_gpt_chat(ANWEISUNG)
    elif eingabe_benutzer.lower() == "x":
        break
    else:
        print(eingabe_benutzer)
