```mermaid
sequenceDiagram
    participant User
    participant dateien_py
    participant file
    
    User->>dateien_py: schreibe_protokol(datei_namen, inhalt_einfuegen)
    dateien_py->>file: open(datei_namen, "a", encoding="utf-8")
    file->>file: write(inhalt_einfuegen)
    file-->>dateien_py: 
    dateien_py-->>User: 
    
    User->>dateien_py: lese_datei(datei_namen)
    dateien_py->>file: open(datei_namen, "r", encoding="utf-8")
    file->>file: readlines()
    file-->>dateien_py: datei_inhalt
    dateien_py-->>User: datei_inhalt
    
    User->>dateien_py: schreibe_datei(datei_namen, inhalt_einfuegen)
    dateien_py->>file: open(datei_namen, "w", encoding="utf-8")
    file->>file: write(inhalt_einfuegen)
    file-->>dateien_py: 
    dateien_py-->>User: 

