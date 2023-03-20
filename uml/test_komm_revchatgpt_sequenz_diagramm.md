```mermaid
sequenceDiagram
    participant User
    participant Chatbot
    User ->> Chatbot: chat_gpt_chat("Hello, GPT!")
    Chatbot ->> Chatbot: configure chatbot with config, conversation_id and parent_id
    Chatbot ->> Chatbot: ask("Hello, GPT!")
    Chatbot ->> Chatbot: return response
    Chatbot -->> User: "Hello, World!"

