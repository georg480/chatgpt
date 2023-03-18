import glob


def schreibe_protokol(datei_namen, inhalt_einfuegen):
    with open(datei_namen, "a", encoding="utf-8") as file:
        file.write(inhalt_einfuegen)


def lese_datei(datei_namen):
    try:
        with open(datei_namen, "r", encoding="utf-8") as file:
            datei_inhalt = " ".join([line.strip() for line in file.readlines()])
            file.flush()  # Puffer leeren und Daten auf die p m# schreiben
    except IOError as exc:
        print(f"Es gab ein Problem beim Lesen der Datei '{datei_namen}': {exc}")
        datei_inhalt = ""
    except Exception as exc:
        print(
            f"Es gab einen unbekannten Fehler beim Lesen der Datei '{datei_namen}': {exc}"
        )
        datei_inhalt = ""
    return datei_inhalt


def schreibe_md(datei_namen, datei_inhalt):
    try:
        with open(datei_namen, "w", encoding="utf-8") as file:
            lines = datei_inhalt[datei_inhalt.index("```") : datei_inhalt.rindex("```")]
            for line in lines.split("\\n', '"):
                print(line + "\n")
                file.write(line + "\n")
            print(f"Name {datei_namen}")
    except IOError as exc:
        print(f"Es gab ein Problem beim Schreiben der Datei '{datei_namen}': {exc}")
    except Exception as exc:
        print(
            f"Es gab einen unbekannten Fehler beim schreiben der Datei '{datei_namen}': {exc}"
        )
        return


def schreibe_datei(datei_namen, inhalt_einfuegen):
    with open(datei_namen, "w", encoding="utf-8") as file:
        file.write(inhalt_einfuegen)


def lese_gesuchte_dateinamen(suchfilter):
    return glob.glob(suchfilter, recursive=True)


def aendere_datei_pfard(datei: str):
    return datei.replace("\\", "/")


def gebe_nur_dateinamen(datei_namen: str):
    return datei_namen.split("/")[-1]
