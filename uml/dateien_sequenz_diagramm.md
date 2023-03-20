```mermaid
sequenceDiagram
    participant Client
    participant lese_datei
    participant Datei

    Client->>lese_datei: datei_namen
    lese_datei->>Datei: öffne Datei
    Datei->>lese_datei: datei_inhalt
    alt Fehler beim Lesen
        lese_datei->>Client: Exception
    else
        lese_datei->>Client: datei_inhalt
    end

