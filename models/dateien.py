import os
def schreibe_protokol(datei_namen, inhalt_einfuegen):
    with open(datei_namen, "a", encoding="utf-8") as file:
        file.write(inhalt_einfuegen)


def lese_datei(datei_namen):
    with open(datei_namen, "r", encoding="utf-8") as file:
        datei_inhalt = file.read()
    return datei_inhalt

