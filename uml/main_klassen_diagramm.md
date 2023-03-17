```
@startuml

class main {
    -MODEL: str
    +__init__()
    +komm_chat()
    +chat(ANWEISUNG: str, MODEL: str, JAHR: int) : str
    +erzeuge_unittest(SKRIPT_NAME: str, MODEL: str) : None
    +erzeuge_uml() : None
    +pruefe_py_gebaut(SKRIPT_NAME: str) : None
}

@enduml

