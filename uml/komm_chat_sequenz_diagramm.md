```mermaid
sequenceDiagram
    participant C as Client
    participant S as Server
    C->>+S: prompt = "Mensch: Erkläre alles auf Deutsch\nAI:"
    loop
        C->>+S: prompt += input("Du: ")
        S->>+S: answer, prompt = gpt3(prompt, temperature=0.9, frequency_penalty=1, presence_penalty=1, start_text="\nAI:", restart_text="\nMensch: ", stop_seq=['"""'])
        S->>-C: "GPT-3:" + answer
    end

