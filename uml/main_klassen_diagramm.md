```plantuml
@startuml

class komm_chat {
    -modell: str
    -anfrage_url: str
    -antwort_url: str
    -session_id: str
    -antwort: str
    +__init__(self, modell: str)
    +sende_anfrage(self, anfrage: str)
    +empfange_antwort(self) -> str
}

class komm_revchatgpt {
    -modell: str
    -anfrage_url: str
    -antwort_url: str
    -session_id: str
    -antwort: str
    +__init__(self, modell: str)
    +sende_anfrage(self, anfrage: str)
    +empfange_antwort(self) -> str
}

class erzeuge_uml {
    -dateiname: str
    -text: str
    +__init__(self, dateiname: str = "main.py")
    +erzeuge_klassendiagramm(self) -> str
    +erzeuge_ablaufdiagramm(self) -> str
}

class erzeuge_unittest {
    -skriptname: str
    -modell: str
    +__init__(self, skriptname: str, modell: str = "davinci")
    +erzeuge_unittest_skript(self) -> str
}

class lese_datei {
    +__init__(self, dateiname: str)
    +lese(self) -> str
}

class schreibe_datei {
    +__init__(self, dateiname: str, inhalt: str)
    +schreibe(self) -> None
}

class pruefe_py_gebaut {
    +__init__(self, skriptname: str)
    +pruefe(self) -> None
}

class functions {
    +pruefe_py_gebaut(skriptname: str) -> None
}

class main {
    -MODEL: str
    +__main__()
}

main --> komm_chat
main --> komm_revchatgpt
main --> erzeuge_uml
main --> erzeuge_unittest
main --> lese_datei
main --> schreibe_datei
main --> pruefe_py_gebaut
main --> functions

@enduml

