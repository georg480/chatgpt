```
@startuml
actor User
User -> functions: pruefe_py_gebaut(skript_name: str)
functions -> subprocess: call("isort .", shell=True)
subprocess --> functions: return
functions -> subprocess: call("black .", shell=True)
subprocess --> functions: return
functions -> subprocess: call("pylint " + skript_name, shell=True)
subprocess --> functions: return
functions -> subprocess: call("pyreverse -a1 -s1  -f ALL -d ALL  .  -o pdf", shell=True)
subprocess --> functions: return
functions -> subprocess: call("pytest", shell=True)
subprocess --> functions: return
functions --> User: Suche nach ERROR und entferne am Ende das init, Fehler und prüfe den Import
@enduml

