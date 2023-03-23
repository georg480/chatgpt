```mermaid
sequenceDiagram
    participant TestCase
    participant os
    participant dateien
    participant schreibe_protokol
    participant lese_datei

    TestCase ->>+ schreibe_protokol: schreibe_protokol(datei_namen, inhalt_einfuegen)
    schreibe_protokol ->>+ os: os.path.exists(datei_namen)
    os -->>- schreibe_protokol: True
    schreibe_protokol ->>+ os: open(datei_namen, "r", encoding="utf-8")
    os -->>- schreibe_protokol: file
    schreibe_protokol ->>+ file: file.read()
    file -->>- schreibe_protokol: inhalt_einfuegen
    TestCase ->>+ lese_datei: lese_datei(datei_namen)
    lese_datei -->>- TestCase: inhalt_einfuegen
    TestCase ->>+ os: os.remove(datei_namen)

