```mermaid
sequenceDiagram
    participant User
    participant gpt3.py
    participant OpenAI API

    User->>gpt3.py: prompt, engine, max_laenge, temperature, top_p, frequency_penalty, presence_penalty, start_text, restart_text, stop_seq
    gpt3.py->>OpenAI API: Completion.create(prompt, engine, max_tokens, temperature, top_p, frequency_penalty, presence_penalty, stop)
    OpenAI API-->>gpt3.py: response
    gpt3.py->>gpt3.py: answer = response.choices[0]["text"]
    gpt3.py->>gpt3.py: new_prompt = prompt + start_text + answer + restart_text
    gpt3.py-->>User: answer, new_prompt

