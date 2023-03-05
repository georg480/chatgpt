from openai_com import chat

MODEL = "text-davinci-003"

while True:
    eingabe_benutzer = input(
        "Frage /Eingabe ein. e (erkläre Code), f (frage),  u (Eng->D), x (aus)"
    )

    if eingabe_benutzer.lower() == "u":
        anweisung = (
            "Translate this into German:\n\n" + input("Englischer Text") + "\n\n"
        )
        antwort = chat(anweisung, MODEL)
        print(f"\n{antwort}")
    elif eingabe_benutzer.lower() == "e":
        anweisung = (
            "Erkläre die Funktion des Codes:\n\n" + input("Eingabe Quellcode") + "\n\n"
        )
        antwort = chat(anweisung, MODEL)
        print(f"\n{antwort}")
    elif eingabe_benutzer.lower() == "f":
        anweisung = input("Eingabe Frage")
        antwort = chat(anweisung, MODEL)
        print(f"\n{antwort}")
    elif eingabe_benutzer.lower() == "x":
        break
    else:
        print(eingabe_benutzer)
