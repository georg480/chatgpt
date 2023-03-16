```mermaid
sequenceDiagram
    participant User
    participant Code
    participant OpenAI API
    User->>+Code: Sendet eine Anfrage mit einer Anweisung
    Code->>+Code: Verarbeitet die Anweisung
    Code->>+OpenAI API: Sendet eine Anfrage mit der Anweisung
    OpenAI API->>+OpenAI API: Generiert eine Antwort
    OpenAI API->>+Code: Sendet die generierte Antwort zurück
    Code->>+Code: Verarbeitet die generierte Antwort
    Code->>+User: Sendet die generierte Antwort zurück

