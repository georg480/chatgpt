```mermaid
sequenceDiagram
    participant User
    participant Dateien

    User ->> Dateien: schreibe_protokol(datei_namen, inhalt_einfuegen)
    activate Dateien
    Dateien -->> User: 

    User ->> Dateien: lese_datei(datei_namen)
    activate Dateien
    Dateien -->> User: datei_inhalt

    User ->> Dateien: schreibe_datei(datei_namen, inhalt_einfuegen)
    activate Dateien
    Dateien -->> User: 

