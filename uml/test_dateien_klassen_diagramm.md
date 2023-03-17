```mermaid
class TestDateien {
    +setUp()
    +tearDown()
    +test_schreibe_protokol()
    +test_lese_datei()
    +test_schreibe_datei()
}

class Dateien {
    +lese_datei(dateiname: str) -> str
    +schreibe_datei(dateiname: str, inhalt: str) -> None
    +schreibe_protokol(dateiname: str, protokoll: str) -> None
}

TestDateien --> Dateien

