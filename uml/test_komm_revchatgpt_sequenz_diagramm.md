```mermaid
sequenceDiagram
    TestChatbot->>+chat: chat("Wie geht es dir?", "text-davinci-003", 100)
    activate chat
    alt OpenAI API response
        chat-->>-TestChatbot: str response
    else Mocked response
        chat--x TestChatbot: str response
    end

