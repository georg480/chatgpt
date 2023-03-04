from models.dateien import schreibe_protokol
from openai_com import chat

model = "text-davinci-003"

while True:
    benutzer_eingabe = input("Frage /Eingabe ein. a(aus), e (erkläre Code), u (Eng->D)")

    if benutzer_eingabe.lower() == "a":
        break
    elif benutzer_eingabe.lower() == "u":
        anweisung = (
            f"Translate this into German:\n\n" + input("Englischer Text") + "\n\n"
        )
        antwort = chat(anweisung, model)
        print(f"\n{antwort}")
    elif benutzer_eingabe.lower() == "e":
        anweisung = (
                f"Erkläre die Funktion des Codes:\n\n" + input("Eingabe Quellcode") + "\n\n"
        )
        antwort = chat(anweisung, model)
        print(f"\n{antwort}")

