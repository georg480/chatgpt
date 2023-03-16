```mermaid
sequenceDiagram
    participant User
    participant Code
    participant OpenAI API
    User->>+Code: Sendet eine Anfrage mit einer Anweisung an den Code
    Code->>+OpenAI API: Sendet eine Anfrage mit der Anweisung an die OpenAI API
    OpenAI API->>+Code: Sendet eine Antwort zurück mit einer generierten Antwort
    Code->>+User: Sendet die generierte Antwort zurück an den Benutzer

