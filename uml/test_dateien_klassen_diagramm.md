```mermaid
classDiagram
    TestDateien <|-- unittest.TestCase
    TestDateien : +setUp()
    TestDateien : +tearDown()
    TestDateien : +test_schreibe_protokol()
    TestDateien : +test_lese_datei()
    TestDateien : +test_schreibe_datei()
    TestDateien --> lese_datei()
    TestDateien --> schreibe_datei()
    TestDateien --> schreibe_protokol()
    lese_datei() : +str
    schreibe_datei() : +None
    schreibe_protokol() : +None

