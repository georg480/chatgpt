import datetime
import json
import os
import shutil
import webbrowser

import pyjokes
import pyttsx3
import requests
import speech_recognition as sr
import wolframalpha
from gtts import gTTS
from playsound import playsound

from komm_chat import komm_chat
from komm_github import git_commit, git_push
from komm_revchatgpt import chat_gpt_chat, erzeuge_uml, erzeuge_unittest
from models.dateien import lese_datei, schreibe_datei
from models.functions import aufnahme, eingabe, pruefe_py_gebaut, gleich_string

engine = pyttsx3.init("sapi5")
volume = engine.getProperty("volume")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)


def sprechen(text):
    ausgabe = gTTS(text=text, lang="de", slow=False)
    ausgabe.save("etc/musik/tts.mp3")
    playsound("etc/musik/tts.mp3")
    os.remove("etc/musik/tts.mp3")

def auswerten_liste(ergebnisse, suche):
    for alternative in ergebnisse['alternative']:
        print(alternative['transcript'])
        if gleich_string(alternative['transcript'], suche):
            print(f"in liste: {suche} = {alternative['transcript']}")
            return True
    print(f"nicht in liste: {suche}")
    return False

ass_name = "Joy"
sprechen("Hey")
sprechen(ass_name)


def username():
    sprechen("helfen?")
   # uname = takeCommand()
    sprechen("Hallo Georg")
    #sprechen(uname)
    columns = shutil.get_terminal_size().columns

    print("#####################".center(columns))
    print("Hallo Georg ")# , uname.center(columns)###)
    print("#####################".center(columns))

    sprechen("helfen")


def takeCommand():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Helfen...")
        r.pause_threshold = 1.2
        audio = r.listen(source)

    try:
        print("auswerten...")
        ausgabe = r.recognize_google(audio, language="DE-de", show_all=True)
        print(f"Benutzer sagt: {ausgabe}\n")
        #sprechen(f"Benutzer sagt: {#}\n")
        return ausgabe

    except Exception as e:
        print(e)
        print("Nicht in deinen Befehlen.")
        sprechen(f"Nicht in deinen Befehlen.{e}")
        return f"Nicht in deinen Befehlen.{e}"
    return [
        {"transcript": "0", "confidence": 0.83590513},
        {"transcript": "1"},
        {"transcript": "2"},
        {"transcript": "3"},
        {"transcript": "4"},
    ]

if __name__ == "__main__":
    reinigen = lambda: os.system("cls")

    reinigen()
    username()

    while True:
        ergebnisse = takeCommand()
        #ergebnisse = [{'transcript': 'mach komm mit', 'confidence': 0.84865618}, {'transcript': 'macht komm mit'}, {'transcript': 'Mark komm mit'}, {'transcript': 'Mark kommet'}]
        # ergebnisse = {'alternative': [{'transcript': 'Marco mit', 'confidence': 0.89634383}, {'transcript': 'mach komm mit'}, {'transcript': 'macht Komet'}, {'transcript': 'mach komm jetzt'}, {'transcript': 'Marco nix'}], 'final': True}
        # Eingabe a(abl), c(com), e(erkl.Code), f(Frage), p(prü), pu(push), t(Unittest.md), u(E->D), x

        if auswerten_liste(ergebnisse, "alles auswerten"):
            erzeuge_uml()
            sprechen("Alles auswerten")
        elif auswerten_liste(ergebnisse, "mach komm mit"):
            git_commit()
            sprechen("mache commit")
        elif auswerten_liste(ergebnisse, "mache erklärung"):
            sprechen("mache erklaerung")
            ANWEISUNG = eingabe("Welche Datei")
            ANWEISUNG = (
                    "Kannst du erkläre"
                    "n, was der Code macht und das Ergebnis als Markdown ausgeben?\n"
                    + lese_datei(ANWEISUNG)
            )
            print(ANWEISUNG)
            ANTWORT = chat_gpt_chat(ANWEISUNG)
        elif auswerten_liste(ergebnisse, "mache unittest"):
            sprechen("mache unittest")
            erzeuge_unittest(eingabe("Skript Name?")[:-3])
        elif auswerten_liste(ergebnisse, "mache pruefung"):
            sprechen("mache pruefung")
            pruefe_py_gebaut(eingabe("Skript Name?"))
        elif auswerten_liste(ergebnisse, "stelle frage"):
            sprechen("stelle frage")
            ANWEISUNG = input("Stelle Frage")  # aufnahme()
            ANTWORT = chat_gpt_chat(ANWEISUNG)
            sprechen(ANTWORT)
        elif auswerten_liste(ergebnisse, "mache update"):
            git_push()
            sprechen("mache push und update")
        elif auswerten_liste(ergebnisse, "uebersetztedatei"):
            sprechen("uebersetzte datei")
            print(lese_datei("englischer_text.txt"))
            ANWEISUNG = (
                    "Translate this into German:\n\n"
                    + lese_datei("englischer_text.txt")
                    + "\n\n"
            )
            ANTWORT = chat_gpt_chat(ANWEISUNG)
            print(f"\n{ANTWORT}")
            schreibe_datei("deutscher_text.txt", ANTWORT)
        else:
            print("Der String ist nicht enthalten.")


