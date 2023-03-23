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
        print(f"User sagt: {query}\n")

    except Exception as e:
        print(e)
        print("Nicht in deinen befehlen.")
        return "None"

    return query



if __name__ == "__main__":
    clear = lambda: os.system("cls")

    # This Function will clean any
    # command before execution of this python file
    clear()
    wishMe()
    username()

    while True:
        query = takeCommand().lower()

        # All the commands said by user will be
        # stored here in 'query' and will be
        # converted to lower case for easily
        # recognition of command

        if "öffne youtube" in query:
            sprechen("öffne Youtube\n")
            webbrowser.open("youtube.com")

        elif "mache updates" in query:
            sprechen("push\n")
            git_push()

        elif "mache Samsung" or "mache komm mit" in query:
            sprechen("commit\n")
            git_commit()

        elif "öffne google" in query:
            sprechen("öffne Google\n")
            webbrowser.open("google.com")


        elif "spiele musik" in query or "spiele lied" in query:
            sprechen("Spiele Musik oder Lied")
            # music_dir = "G:\\Song"
            music_dir = r"C:\Users\georg\Seafile\Meine Bibliothek-008100\Musik"
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[1]))

        elif "open opera" in query:
            codePath = (
                r"C:\\Users\\GEORG\\AppD"
                r""
                r"ata\\Local\\Programs\\Opera\\launcher.exe"
            )
            os.startfile(codePath)

        elif "sage uhrzeit" in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            print(f"Hey die Zeit {strTime}")
            sprechen(f"Hey die Zeit {strTime}")

        elif "ändere den namen zu" in query:
            query = query.replace("Ändere den Namen zu", "")
            assname = query

        elif "ändere name" in query:
            sprechen("What would you like to call me, Sir ")
            assname = takeCommand()
            sprechen("Thanks for naming me")

        elif "beenden" in query:
            sprechen("Danke für deine Zeit")


        elif "wo bist du erstellt" in query or "who created you" in query:
            sprechen("Ich komme aus Sonsbeck.")

        elif "erzähle witz" in query:
            sprechen(pyjokes.get_joke())

        elif "suche" in query or "play" in query:
            query = query.replace("suche", "")
            query = query.replace("play", "")
            webbrowser.open(query)

        elif "wetter" in query:
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

        elif "öffne wikipedia" in query:
            webbrowser.open("wikipedia.com")

        elif "Good Morning" in query:
            sprechen("A warm" + query)
            sprechen("How are you Mister")
            sprechen(assname)

        # most asked question from google Assistant
        elif "will you be my gf" in query or "will you be my bf" in query:
            sprechen("I'm not sure about, may be you should give me some time")

        elif "lauter" in query:
            volume = engine.getProperty('volume')
            print(f"volume: {volume}")
            engine.setProperty('volume', volume + 0.25)
            sprechen("Georg lauter")

        elif "leiser" in query:
            volume = engine.getProperty('volume')
            print(f"volume: {volume}")
            engine.setProperty('volume', volume - 0.25)
            sprechen("Georg leiser")

        elif "unterbreche" in query:
            sprechen("unterbreche")

        elif "weiter" in query:
            sprechen("weiter")

        elif "what is" in query or "who is" in query:
            # Use the same API key
            # that we have generated earlier
            client = wolframalpha.Client("API_ID")
            res = client.query(query)

            try:
                print(next(res.results).text)
                sprechen(next(res.results).text)
            except StopIteration:
                print("No results")

    # elif "" in query:
    # Command go here
    # For adding more commands
