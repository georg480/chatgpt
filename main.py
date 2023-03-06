from komm_chat import komm_chat
from openai_com import chat

MODEL = "text-davinci-003"

while True:
    eingabe_benutzer = input(
        "Frage /Eingabe ein. c (chat), e (erkläre Code), f (frage),  u (Eng->D), x (aus)"
    )

    if eingabe_benutzer.lower() == "u":
        anweisung = (
            "Translate this into German:\n\n" + input("Englischer Text") + "\n\n"
        )
        antwort = chat(anweisung, MODEL)
        print(f"\n{antwort}")
    elif eingabe_benutzer.lower() == "c":
        komm_chat()
    elif eingabe_benutzer.lower() == "f":
        anweisung = input("Eingabe Frage")
        antwort = chat(anweisung, MODEL)
        print(f"\n{antwort}")
    elif eingabe_benutzer.lower() == "x":
        break
    else:
        print(eingabe_benutzer)
