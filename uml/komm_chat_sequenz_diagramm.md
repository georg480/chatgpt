```mermaid
sequenceDiagram
    participant Mensch
    participant AI
    Mensch->>AI: "Erkläre alles auf Deutsch"
    loop
        Mensch->>AI: Du:
        AI->>Mensch: GPT-3: Antwort
    end

