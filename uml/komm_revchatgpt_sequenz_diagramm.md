sequenceDiagram
participant User
participant chat()
participant schreibe_protokol()
participant Chatbot

    User->>chat(): stellt eine Anfrage an den Chatbot
    chat()->>schreibe_protokol(): speichert die Anfrage im Protokoll
    chat()->>Chatbot: ruft die Methode ask() auf
    Chatbot->>Chatbot: verarbeitet die Anfrage
    Chatbot-->>chat(): gibt eine Antwort zurück
    chat()->>schreibe_protokol(): speichert die Antwort im Protokoll
    chat()->>User: gibt die Antwort zurück
