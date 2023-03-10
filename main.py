import os

from komm_chat import komm_chat
from models.dateien import lese_datei, schreibe_datei
from models.functions import pruefe_py_gebaut
from openai_com import chat, erzeuge_unittest

MODEL = "text-davinci-003"

while True:
    eingabe_benutzer = input(
        "Eingabe c(chat), e(erkl.Code), f(Frage), p(prü), t(Unittest), u(E->D), x"
    )
    if eingabe_benutzer.lower() == "u":
        print(lese_datei("englischer_text.txt"))
        anweisung = (
            "Translate this into German:\n\n"
            + lese_datei("englischer_text.txt")
            + "\n\n"
        )
        antwort = chat(anweisung, MODEL)
        print(f"\n{antwort}")
        schreibe_datei("deutscher_text.txt", antwort)
    elif eingabe_benutzer.lower() == "c":
        komm_chat()
    elif eingabe_benutzer.lower() == "t":
        erzeuge_unittest(input("Skript Name?"), MODEL)
    elif eingabe_benutzer.lower() == "p":
        pruefe_py_gebaut(input("Skript Name?"))
    elif eingabe_benutzer.lower() == "f":
        anweisung = input("Eingabe Frage")
        antwort = chat(anweisung, MODEL)
    elif eingabe_benutzer.lower() == "e":
        anweisung = input("Welche Datei")
        anweisung = "Erkläre die Funktion des Codes. \n" + lese_datei(anweisung)
        print(anweisung)
        antwort = chat(anweisung, MODEL)
    elif eingabe_benutzer.lower() == "x":
        break
    else:
        print(eingabe_benutzer)
