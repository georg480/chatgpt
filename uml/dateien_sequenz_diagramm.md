```mermaid
sequenceDiagram
    participant User
    participant FileModule
    User->>+FileModule: schreibe_protokol(datei_namen, inhalt_einfuegen)
    activate FileModule
    FileModule->>+File: open(datei_namen, "a", encoding="utf-8")
    activate File
    File->>+File: write(inhalt_einfuegen)
    deactivate File
    FileModule->>-File: close()
    deactivate FileModule
    User->>+FileModule: lese_datei(datei_namen)
    activate FileModule
    FileModule->>+File: open(datei_namen, "r", encoding="utf-8")
    activate File
    File->>+File: readlines()
    File-->>-FileModule: list of lines
    File->>+File: close()
    deactivate File
    FileModule->>-File: close()
    deactivate FileModule
    User->>+FileModule: schreibe_datei(datei_namen, inhalt_einfuegen)
    activate FileModule
    FileModule->>+File: open(datei_namen, "w", encoding="utf-8")
    activate File
    File->>+File: write(inhalt_einfuegen)
    deactivate File
    FileModule->>-File: close()
    deactivate FileModule

