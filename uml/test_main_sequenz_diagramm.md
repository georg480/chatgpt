sequenceDiagram
participant Benutzer
participant main.py
participant komm_revchatgpt.py
participant komm_chat.py
participant models.dateien.py
participant models.functions.py
Benutzer->>main.py: Eingabe a(abl), e(erkl.Code), f(Frage), p(prü), t(Unittest), u(E->D), x
main.py->>komm_revchatgpt.py: if eingabe_benutzer.lower() == "u"
komm_revchatgpt.py->>models.dateien.py: lese_datei("englischer_text.txt")
models.dateien.py-->>komm_revchatgpt.py: Text als Rückgabewert
komm_revchatgpt.py->>komm_revchatgpt.py: ANWEISUNG = "Translate this into German:\n\n" + Text + "\n\n"
komm_revchatgpt.py->>komm_revchatgpt.py: ANTWORT = chat(ANWEISUNG, MODEL, 2035)
komm_revchatgpt.py->>models.dateien.py: schreibe_datei("deutscher_text.txt", ANTWORT)
main.py->>komm_revchatgpt.py: elif eingabe_benutzer.lower() == "a"
komm_revchatgpt.py->>komm_revchatgpt.py: erzeuge_uml()
main.py->>komm_chat.py: elif eingabe_benutzer.lower() == "c"
komm_chat.py-->>Benutzer: Chat-Schnittstelle
main.py->>komm_revchatgpt.py: elif eingabe_benutzer.lower() == "t"
main.py->>komm_revchatgpt.py: erzeuge_unittest(input("Skript Name?"), MODEL)
main.py->>models.functions.py: elif eingabe_benutzer.lower() == "p"
models.functions.py-->>Benutzer: Rückmeldung ob Skript gebaut wurde
main.py->>komm_revchatgpt.py: elif eingabe_benutzer.lower() == "f"
Benutzer->>main.py: Eingabe Frage
main.py->>komm_revchatgpt.py: ANWEISUNG = input("Eingabe Frage")
komm_revchatgpt.py->>komm_revchatgpt.py: ANTWORT = chat(ANWEISUNG, MODEL, 2035)
main.py->>komm_revchatgpt.py: elif eingabe_benutzer.lower() == "e"
Benutzer->>main.py: Welche Datei
main.py->>models.dateien.py: ANWEISUNG = input("Welche Datei")
models.dateien.py->>models.dateien.py: ANWEISUNG = "Kannst du bitte ein UML Ablaufdiagramm erstellen und das Ergebnis als Markdown ausgeben?\n" + lese_datei(ANWEISUNG)
models.dateien.py->>komm_revchatgpt.py: ANTWORT = chat(ANWEISUNG, MODEL, 2035)
main.py->>main.py: else
main.py->>Benutzer: eingabe_benutzer
main.py->
