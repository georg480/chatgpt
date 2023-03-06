import subprocess


def teste_py_gebaut(skript_name: str):
    subprocess.call("isort .", shell=True)
    subprocess.call("black .", shell=True)
    subprocess.call("pylint " + skript_name, shell=True)
    subprocess.call("pytest", shell=True)


def plus(in1: int, in2: int):
    return in1 + in2


def minus(in1: int, in2: int):
    return in1 - in2


def teilen(in1: int, in2: int):
    return in1 / in2


def mal(in1: int, in2: int):
    return in1 * in2


print(plus(2, 3))
print(minus(2, 3))
print(mal(2, 3))
print(teilen(2, 3))
