```mermaid
sequenceDiagram
    participant User
    participant chat
    User->>chat: chat("Wie geht es dir?", "text-davinci-003", 100)
    chat->>builtins.input: input()
    builtins.input-->>chat: "Wie geht es dir?"
    chat->>Davinci API: OpenAI request
    Davinci API-->>chat: Response
    chat-->>User: response

