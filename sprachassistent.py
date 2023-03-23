import datetime
import os
import shutil
import webbrowser

import pyjokes
import pyttsx3
from gtts import gTTS
from playsound import playsound
from komm_github import git_commit, git_push
import requests
import speech_recognition as sr
import wolframalpha

engine = pyttsx3.init("sapi5")
volume = engine.getProperty('volume')
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)

def sprechen(text):
    ausgabe = gTTS(text=text, lang='de', slow=False)
    ausgabe.save("etc/musik/tts.mp3")
    playsound("etc/musik/tts.mp3")
    os.remove("etc/musik/tts.mp3")

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        sprechen("Hey ")

    elif hour >= 12 and hour < 18:
        sprechen("hey !")

    else:
        sprechen("hey !")

    ass_name = "Joy"
    sprechen("Wie kann ich helfen? ")
    sprechen(ass_name)


def username():
    sprechen("helfen?")
    uname = takeCommand()
    sprechen("Hallo Georg")
    sprechen(uname)
    columns = shutil.get_terminal_size().columns

    print("#####################".center(columns))
    print("Hallo Georg ", uname.center(columns))
    print("#####################".center(columns))

    sprechen("helfen")


def takeCommand():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Helfen...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("auswerten...")
        query = r.recognize_google(audio, language="DE-de")
        print(f"Benutzer sagt: {query}\n")
        sprechen(f"Benutzer sagt: {query}\n")

    except Exception as e:
        print(e)
        print("Nicht in deinen Befehlen.")
        sprechen(f"Nicht in deinen Befehlen.{e}")
        return f"Nicht in deinen Befehlen.{e}"

    return query



if __name__ == "__main__":
    clear = lambda: os.system("cls")

    # This Function will clean any
    # command before execution of this python file
    clear()
    wishMe()
    username()

    while True:
        commando = takeCommand().lower()

        # All the commands said by user will be
        # stored here in 'query' and will be
        # converted to lower case for easily
        # recognition of command

        if "öffne youtube" in commando:
            sprechen("öffne Youtube\n")
            webbrowser.open("youtube.com")

        elif "mache updates" in commando:
            sprechen("mache push und update\n")
            eingabe_test = input("push ausgerufen?")
            git_push()

        elif "mache komm mit" in commando:
            sprechen("mache commit\n")
            eingabe_test = input("commit ausgerufen?")
            git_commit()

        elif "öffne google" in commando:
            sprechen("öffne Google\n")
            webbrowser.open("google.com")


        elif "spiele musik" in commando or "spiele lied" in commando:
            sprechen("Spiele Musik oder Lied")
            # music_dir = "G:\\Song"
            music_dir = r"C:\Users\georg\Seafile\Meine Bibliothek-008100\Musik"
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[1]))

        elif "open opera" in commando:
            codePath = (
                r"C:\\Users\\GEORG\\AppD"
                r""
                r"ata\\Local\\Programs\\Opera\\launcher.exe"
            )
            os.startfile(codePath)

        elif "sage uhrzeit" in commando:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            print(f"Hey die Zeit {strTime}")
            sprechen(f"Hey die Zeit {strTime}")

        elif "ändere den namen zu" in commando:
            commando = commando.replace("Ändere den Namen zu", "")
            assname = commando

        elif "ändere name" in commando:
            sprechen("What would you like to call me, Sir ")
            assname = takeCommand()
            sprechen("Thanks for naming me")

        elif "beenden" in commando:
            sprechen("Danke für deine Zeit")


        elif "wo bist du erstellt" in commando or "who created you" in commando:
            sprechen("Ich komme aus Sonsbeck.")

        elif "erzähle witz" in commando:
            sprechen(pyjokes.get_joke())

        elif "suche" in commando or "play" in commando:
            commando = commando.replace("suche", "")
            commando = commando.replace("play", "")
            webbrowser.open(commando)

        elif "wetter" in commando:
            # Google Open weather website
            # to get API of Open weather
            api_key = "64534252b0c9839708f6afcb08ff7b65"
            base_url = "http://api.openweathermap.org/data/2.5/weather?"
            # speak(" Stadt name ")
            # print(" Stadt name : ")
            # city_name = takeCommand()
            complete_url = base_url + "appid=" + api_key + "&q=sonsbeck"  # + city_name
            response = requests.get(complete_url)
            x = response.json()

            if x["code"] != "404":
                y = x["main"]
                current_temperature = y["temp"]
                current_pressure = y["pressure"]
                current_humidiy = y["humidity"]
                z = x["weather"]
                weather_description = z[0]["description"]
                print(
                    " Temperature (in kelvin unit) = "
                    + str(current_temperature)
                    + "\n atmospheric pressure (in hPa unit) ="
                    + str(current_pressure)
                    + "\n humidity (in percentage) = "
                    + str(current_humidiy)
                    + "\n description = "
                    + str(weather_description)
                )

            else:
                sprechen(" City Not Found ")

        elif "öffne wikipedia" in commando:
            webbrowser.open("wikipedia.com")

        elif "Good Morning" in commando:
            sprechen("A warm" + commando)
            sprechen("How are you Mister")
            sprechen(assname)

        # most asked question from google Assistant
        elif "will you be my gf" in commando or "will you be my bf" in commando:
            sprechen("I'm not sure about, may be you should give me some time")

        elif "lauter" in commando:
            volume = engine.getProperty('volume')
            print(f"volume: {volume}")
            engine.setProperty('volume', volume + 0.25)
            sprechen("Georg lauter")

        elif "leiser" in commando:
            volume = engine.getProperty('volume')
            print(f"volume: {volume}")
            engine.setProperty('volume', volume - 0.25)
            sprechen("Georg leiser")

        elif "unterbreche" in commando:
            sprechen("unterbreche")

        elif "weiter" in commando:
            sprechen("weiter")

        else:
            print("kenne kein Befehl: {commando}")
            sprechen("kenne kein Befehl: {commando}")


    # elif "" in query:
    # Command go here
    # For adding more commands
