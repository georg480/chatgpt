```mermaid
sequenceDiagram
    participant User
    participant AI
    participant OpenAI

    User ->> AI: Mensch: Erkläre alles auf Deutsch
    loop
        User ->> AI: Du: ...
        AI ->> OpenAI: gpt3(prompt, ...)
        OpenAI -->> AI: response
        AI ->> AI: answer = response.choices[0]["text"]
        AI ->> AI: new_prompt = prompt + start_text + answer + restart_text
        AI ->> User: GPT-3: answer
    end

