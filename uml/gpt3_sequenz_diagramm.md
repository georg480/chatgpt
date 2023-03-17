```mermaid
sequenceDiagram
    participant User
    participant openai
    User ->> openai: openai.api_key = os.getenv("OPENAI_API_KEY")
    User ->> openai: gpt3()
    openai ->> openai: openai.Completion.create()
    openai ->> User: answer

