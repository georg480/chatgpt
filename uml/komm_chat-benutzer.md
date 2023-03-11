sequenceDiagram
participant Benutzer
participant OpenAI API
participant komm_chat() Funktion

    Benutzer->>komm_chat(): gibt Eingabeaufforderung ein
    komm_chat()->>OpenAI API: sendet Eingabeaufforderung an API
    OpenAI API-->>komm_chat(): sendet Antwort zurück
    komm_chat()-->>Benutzer: gibt Antwort aus
