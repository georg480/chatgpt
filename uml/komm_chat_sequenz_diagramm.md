```
sequenceDiagram
    participant User
    participant GPT-3
    User->>+GPT-3: prompt = "Mensch: Erkläre alles auf Deutsch\nAI: "
    loop
        User->>+GPT-3: input
        GPT-3->>+GPT-3: prompt += input
        GPT-3->>+GPT-3: gpt3(prompt, temperature=0.9, frequency_penalty=1, presence_penalty=1, start_text="\\nAI:", restart_text="\\nMensch: ", stop_seq=[\'"""\'])
        GPT-3-->>-User: answer
        User: print("GPT-3:" + answer)
    end

