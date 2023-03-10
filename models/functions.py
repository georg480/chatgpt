import subprocess


def pruefe_py_gebaut(skript_name: str):
    subprocess.call("isort .", shell=True)
    subprocess.call("black .", shell=True)
    subprocess.call("pylint " + skript_name, shell=True)
    subprocess.call("pyreverse -a1 -s1  -f ALL -d ALL  .  -o pdf", shell=True)
    subprocess.call("pytest", shell=True)
    print("Suche nach ERROR und entferne am Ende das init, Fehler und prüfe den Import")


def plus(in1: int, in2: int):
    return in1 + in2


def minus(in1: int, in2: int):
    return in1 - in2


def teilen(in1: int, in2: int):
    return in1 / in2


def mal(in1: int, in2: int):
    return in1 * in2
