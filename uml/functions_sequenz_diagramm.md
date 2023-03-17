```
@startuml
title UML Sequence Diagram: models/functions.py

actor User

User -> functions: pruefe_py_gebaut(skript_name: str)

activate functions

functions -> subprocess: call("isort .", shell=True)
subprocess -> subprocess: sort imports

functions -> subprocess: call("black .", shell=True)
subprocess -> subprocess: format code

functions -> subprocess: call("pylint " + skript_name, shell=True)
subprocess -> subprocess: run pylint on script

functions -> subprocess: call("pyreverse -a1 -s1  -f ALL -d ALL  .  -o pdf", shell=True)
subprocess -> subprocess: generate UML class diagram

functions -> subprocess: call("pytest", shell=True)
subprocess -> subprocess: run tests with pytest

functions -> User: Suche nach ERROR und entferne am Ende das init, Fehler und prüfe den Import
deactivate functions
@enduml

