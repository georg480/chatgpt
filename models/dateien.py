import os


def schreibe_protokol(datei_namen, inhalt_einfuegen):
    with open(datei_namen, "a", encoding="utf-8") as file:
        file.write(inhalt_einfuegen)


def lese_datei(datei_namen):
    try:
        with open(datei_namen, "r", encoding="utf-8") as file:
            datei_inhalt = " ".join([line.strip() for line in file.readlines()])
            file.flush()  # Puffer leeren und Daten auf die Festplatte schreiben
    except IOError as e:
        print(f"Es gab ein Problem beim Lesen der Datei '{datei_namen}': {e}")
        datei_inhalt = ""
    except Exception as e:
        print(
            f"Es gab einen unbekannten Fehler beim Lesen der Datei '{datei_namen}': {e}"
        )
        datei_inhalt = ""
    return datei_inhalt


def schreibe_datei(datei_namen, inhalt_einfuegen):
    with open(datei_namen, "w", encoding="utf-8") as file:
        file.write(inhalt_einfuegen)
