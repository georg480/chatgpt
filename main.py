from openai_com import chat

MODEL = "text-davinci-003"

while True:
    benutzer_eingabe = input("Frage /Eingabe ein. x(aus), e (erkläre Code), u (Eng->D)")

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
    elif benutzer_eingabe.lower() == "c":
        anweisung = input("Eingabe Frage")
        antwort = chat(anweisung, MODEL)
        print(f"\n{antwort}")
    elif benutzer_eingabe.lower() == "x":
        break
    else:
        print(benutzer_eingabe)


print("hi")


print("test git new Branch")