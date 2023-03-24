import os
import subprocess

import speech_recognition as sr


def pruefe_py_gebaut(skript_name: str):
    subprocess.call("isort .", shell=True)
    subprocess.call("black .", shell=True)
    subprocess.call("pylint " + skript_name, shell=True)
    subprocess.call("pytest", shell=True)
    print("Suche nach ERROR und entferne am Ende das init, Fehler und prüfe den Import")

def gleich_string(string1, string2):
    if len(string1) == len(string2) and string1 == string2:
        return True
    else:
        return False


def eingabe(anzeige: str):
    while True:
        eingabe = input(anzeige)
        if not eingabe:
            print("Die Eingabe darf nicht leer sein!")
        else:
            print("Ihre Eingabe war: ", eingabe)
            return eingabe
            break


import speech_recognition as sr

recognizer = sr.Recognizer()

""" recording the sound """


def aufnahme():
    with sr.Microphone() as source:
        print("Warte.. Umgebebungsgeräusche auto")
        recognizer.adjust_for_ambient_noise(source, duration=1)
        print("Aufzeichnung.. (15 Sekunden Pausenzeit)")
        recorded_audio = recognizer.listen(source, timeout=15)
        print("Aufzeichnung fertig")

    """ Recorgnizing the Audio """
    try:
        print("Recognizing the text")
        text = recognizer.recognize_google(recorded_audio, language="de-DE")
        print("Decoded Text : {}".format(text))
        return "Decoded Text : {}".format(text)

    except Exception as ex:
        print(ex)


from gtts import gTTS
from playsound import playsound


def sprechen(text):
    ausgabe = gTTS(text=text, lang="de", slow=False)
    ausgabe.save("etc/musik/tts.mp3")
    playsound("etc/musik/tts.mp3")
    os.remove("etc/musik/tts.mp3")


# sprechen("Hallo")

# Python program to translate
# speech to text and text to speech
#
# import os
# from pydub import AudioSegment
# import speech_recognition as sr
# from pydub.silence import split_on_silence
#
# recognizer = sr.Recognizer()
#
# def load_chunks(filename):
#     long_audio = AudioSegment.from_mp3(filename)
#     audio_chunks = split_on_silence(
#         long_audio, min_silence_len=1800,
#         silence_thresh=-17
#     )
#     return audio_chunks
#
# for audio_chunk in load_chunks('aufnahme.mp3'):
#     audio_chunk.export("temp", format="wav")
#     with sr.AudioFile("temp") as source:
#         audio = recognizer.listen(source)
#         try:
#             text = recognizer.recognize_google(audio)
#             print("Chunk : {}".format(text))
#         except Exception as ex:
#             print("Error occured")
#             print(ex)
#
# print("++++++")
