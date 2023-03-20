```mermaid
sequenceDiagram
    participant User
    participant komm_chat
    participant GPT-3

    User ->> komm_chat: "Was ist das Wetter heute?"
    komm_chat ->> GPT-3: "Was ist das Wetter heute?"
    GPT-3 ->> komm_chat: "Das Wetter heute ist sonnig."
    komm_chat ->> User: "GPT-3:Das Wetter heute ist sonnig."

    User ->> komm_chat: "Was ist deine Lieblingsfarbe?"
    komm_chat ->> GPT-3: "Was ist deine Lieblingsfarbe?"
    GPT-3 ->> komm_chat: "Meine Lieblingsfarbe ist Blau."
    komm_chat ->> User: "GPT-3:Meine Lieblingsfarbe ist Blau."

