```mermaid
sequenceDiagram
    participant User
    participant chatbot
    User->>chatbot: chat("Wie geht es dir?", "text-davinci-003", 100)
    activate chatbot
    chatbot-->>User: response
    deactivate chatbot

