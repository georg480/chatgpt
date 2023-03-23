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
    if not isinstance(ergebnisse, list):
        return False
    for ergebnis in ergebnisse:
        if gleich_string(ergebnis["transcript"], suche):
            print(f"in liste: {suche}")
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
        ergebnisse = [{'transcript': 'mach komm mit', 'confidence': 0.84865618}, {'transcript': 'macht komm mit'}, {'transcript': 'Mark komm mit'}, {'transcript': 'Mark kommet'}]
        print(ergebnisse)
        # ergebnisse = [
        #     {"transcript": "mache update", "confidence": 0.83590513},
        #     {"transcript": "ma"},
        #     {"transcript": "mache jetzt"},
        #     {"transcript": "mache eins"},
        #     {"transcript": "kk"},
        # ]
        # # Eingabe a(abl), c(com), e(erkl.Code), f(Frage), p(prü), pu(push), t(Unittest.md), u(E->D), x

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

    #
    #
    #
    #
    #
    #     # All the commands said by user will be
    #     # stored here in 'query' and will be
    #     # converted to lower case for easily
    #     # recognition of command
    #
    #     if "öffne youtube" in commando:
    #         sprechen("öffne Youtube\n")
    #         webbrowser.open("youtube.com")
    #
    #     elif "mache updates" in commando:
    #        # sprechen("mache push und update\n")
    #         eingabe_test = input("push ausgerufen?")
    #         git_push()
    #
    #     elif "mache komm mit" in commando:
    #         sprechen("mache commit\n")
    #         eingabe_test = input("commit ausgerufen?")
    #         git_commit()
    #
    #     elif "öffne google" in commando:
    #         sprechen("öffne Google\n")
    #         webbrowser.open("google.com")
    #
    #
    #     elif "spiele musik" in commando or "spiele lied" in commando:
    #         sprechen("Spiele Musik oder Lied")
    #         # music_dir = "G:\\Song"
    #         music_dir = r"C:\Users\georg\Seafile\Meine Bibliothek-008100\Musik"
    #         songs = os.listdir(music_dir)
    #         print(songs)
    #         os.startfile(os.path.join(music_dir, songs[1]))
    #
    #     elif "open opera" in commando:
    #         codePath = (
    #             r"C:\\Users\\GEORG\\AppD"
    #             r""
    #             r"ata\\Local\\Programs\\Opera\\launcher.exe"
    #         )
    #         os.startfile(codePath)
    #
    #     elif "sage uhrzeit" in commando:
    #         strTime = datetime.datetime.now().strftime("%H:%M:%S")
    #         print(f"Hey die Zeit {strTime}")
    #         sprechen(f"Hey die Zeit {strTime}")
    #
    #     elif "ändere den namen zu" in commando:
    #         commando = commando.replace("Ändere den Namen zu", "")
    #         assname = commando
    #
    #     elif "ändere name" in commando:
    #         sprechen("What would you like to call me, Sir ")
    #         assname = takeCommand()
    #         sprechen("Thanks for naming me")
    #
    #     elif "beenden" in commando:
    #         sprechen("Danke für deine Zeit")
    #
    #
    #     elif "wo bist du erstellt" in commando or "who created you" in commando:
    #         sprechen("Ich komme aus Sonsbeck.")
    #
    #     elif "erzähle witz" in commando:
    #         sprechen(pyjokes.get_joke())
    #
    #     elif "suche" in commando or "play" in commando:
    #         commando = commando.replace("suche", "")
    #         commando = commando.replace("play", "")
    #         webbrowser.open(commando)
    #
    #     elif "wetter" in commando:
    #         # Google Open weather website
    #         # to get API of Open weather
    #         api_key = "64534252b0c9839708f6afcb08ff7b65"
    #         base_url = "http://api.openweathermap.org/data/2.5/weather?"
    #         # speak(" Stadt name ")
    #         # print(" Stadt name : ")
    #         # city_name = takeCommand()
    #         complete_url = base_url + "appid=" + api_key + "&q=sonsbeck"  # + city_name
    #         response = requests.get(complete_url)
    #         x = response.json()
    #
    #         if x["code"] != "404":
    #             y = x["main"]
    #             current_temperature = y["temp"]
    #             current_pressure = y["pressure"]
    #             current_humidiy = y["humidity"]
    #             z = x["weather"]
    #             weather_description = z[0]["description"]
    #             print(
    #                 " Temperature (in kelvin unit) = "
    #                 + str(current_temperature)
    #                 + "\n atmospheric pressure (in hPa unit) ="
    #                 + str(current_pressure)
    #                 + "\n humidity (in percentage) = "
    #                 + str(current_humidiy)
    #                 + "\n description = "
    #                 + str(weather_description)
    #             )
    #
    #         else:
    #             sprechen(" City Not Found ")
    #
    #     elif "öffne wikipedia" in commando:
    #         webbrowser.open("wikipedia.com")
    #
    #     elif "Good Morning" in commando:
    #         sprechen("A warm" + commando)
    #         sprechen("How are you Mister")
    #         sprechen(assname)
    #
    #     # most asked question from google Assistant
    #     elif "will you be my gf" in commando or "will you be my bf" in commando:
    #         sprechen("I'm not sure about, may be you should give me some time")
    #
    #     elif "lauter" in commando:
    #         volume = engine.getProperty('volume')
    #         print(f"volume: {volume}")
    #         engine.setProperty('volume', volume + 0.25)
    #         sprechen("Georg lauter")
    #
    #     elif "leiser" in commando:
    #         volume = engine.getProperty('volume')
    #         print(f"volume: {volume}")
    #         engine.setProperty('volume', volume - 0.25)
    #         sprechen("Georg leiser")
    #
    #     elif "unterbreche" in commando:
    #         sprechen("unterbreche")
    #
    #     elif "weiter" in commando:
    #         sprechen("weiter")
    #
    #     else:
    #         print("kenne kein Befehl: {commando}")
    #         sprechen("kenne kein Befehl: {commando}")

    # elif "" in query:
    # Command go here
    # For adding more commands
