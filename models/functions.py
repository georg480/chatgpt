import subprocess


def pruefe_py_gebaut(skript_name: str):
    subprocess.call("isort .", shell=True)
    subprocess.call("black .", shell=True)
    subprocess.call("pylint " + skript_name, shell=True)
    subprocess.call("pytest", shell=True)
    print("Suche nach ERROR und entferne am Ende das init, Fehler und prüfe den Import")


def eingabe(anzeige: str):
    while True:
        eingabe = input(anzeige)
        if not eingabe:
            print("Die Eingabe darf nicht leer sein!")
        else:
            print("Ihre Eingabe war: ", eingabe)
            return eingabe
            break
