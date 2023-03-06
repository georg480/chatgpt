import os

from komm_chat import komm_chat
from openai_com import chat, erzeuge_unittest

MODEL = "text-davinci-003"

while True:
    eingabe_benutzer = input(
        "Eingabe c(chat), e(erkl.Code), f(Frage), t(Unittest), u(E->D), x(en)"
    )
    if eingabe_benutzer.lower() == "u":
        anweisung = (
            "Translate this into German:\n\n" + input("Englischer Text") + "\n\n"
        )
        antwort = chat(anweisung, MODEL, 150)
        print(f"\n{antwort}")
    elif eingabe_benutzer.lower() == "c":
        komm_chat()
    elif eingabe_benutzer.lower() == "t":
        erzeuge_unittest(input("Skript Name?"), MODEL)
    elif eingabe_benutzer.lower() == "f":
        anweisung = input("Eingabe Frage")
        antwort = chat(anweisung, MODEL, 150)
        print(f"\n{antwort}")
    elif eingabe_benutzer.lower() == "x":
        break
    else:
        print(eingabe_benutzer)
