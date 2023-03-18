```mermaid
sequenceDiagram
    participant TestGPT3
    participant gpt3
    TestGPT3 ->>+ gpt3: prompt
    gpt3 -->>- TestGPT3: answer, new_prompt
    TestGPT3 ->>+ gpt3: answer
    gpt3 -->>- TestGPT3: processed answer

