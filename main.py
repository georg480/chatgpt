from openai_com import chat

MODEL = "text-davinci-003"

while True:
    benutzer_eingabe = input(
        "Frage /Eingabe ein. e (erkläre Code), f (frage),  u (Eng->D), x (aus)"
    )

    if benutzer_eingabe.lower() == "u":
        anweisung = (
            "Translate this into German:\n\n" + input("Englischer Text") + "\n\n"
        )
        antwort = chat(anweisung, MODEL)
        print(f"\n{antwort}")
    elif benutzer_eingabe.lower() == "e":
        anweisung = (
            "Erkläre die Funktion des Codes:\n\n" + input("Eingabe Quellcode") + "\n\n"
        )
        antwort = chat(anweisung, MODEL)
        print(f"\n{antwort}")
    elif benutzer_eingabe.lower() == "f":
        anweisung = input("Eingabe Frage")
        antwort = chat(anweisung, MODEL)
        print(f"\n{antwort}")
    elif benutzer_eingabe.lower() == "x":
        break
    else:
        print(benutzer_eingabe)
