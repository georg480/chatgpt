```mermaid
sequenceDiagram
    participant App
    participant FileIO
    App->>FileIO: schreibe_protokol(datei_namen, inhalt_einfuegen)
    FileIO->>FileIO: öffne Datei im Anhänge-Modus
    FileIO->>FileIO: schreibe Inhalt in Datei
    FileIO-->>App: Protokoll erfolgreich geschrieben
    App->>FileIO: lese_datei(datei_namen)
    FileIO->>FileIO: öffne Datei im Lese-Modus
    FileIO->>FileIO: lese Inhalt der Datei
    FileIO-->>App: Dateiinhalt zurückgegeben
    App->>FileIO: schreibe_md(datei_namen, datei_inhalt)
    FileIO->>FileIO: öffne Datei im Schreib-Modus
    FileIO->>FileIO: extrahiere Code-Abschnitt aus Dateiinhalt
    FileIO->>FileIO: schreibe Code-Abschnitt in Datei
    FileIO-->>App: Markdown-Datei erfolgreich geschrieben

