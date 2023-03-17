```plantuml
@startuml

class TestDateien {
    +setUp()
    +tearDown()
    +test_schreibe_protokol()
    +test_lese_datei()
    +test_schreibe_datei()
}

class dateien {
    +lese_datei(dateipfad: str) -> str
    +schreibe_datei(dateipfad: str, inhalt: str)
    +schreibe_protokol(dateipfad: str, protokoll: str)
}

TestDateien --> dateien

@enduml

