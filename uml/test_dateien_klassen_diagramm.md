```mermaid
class TestDateien {
    +setUp()
    +tearDown()
    +test_schreibe_protokol()
    +test_lese_datei()
    +test_schreibe_datei()
}

class Dateien {
    +lese_datei(datei: str) -> str
    +schreibe_datei(datei: str, inhalt: str) -> None
    +schreibe_protokol(datei: str, inhalt: str) -> None
}

TestDateien -> Dateien

