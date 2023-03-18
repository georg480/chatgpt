```markdown
# KommChat

## Sequenzdiagramm
participant Client
participant Gpt3

Client -> Gpt3: komm_chat()
Gpt3 -> Client: prompt = "Mensch: Erkläre alles auf Deutsch AI: Mensch:"
loop
    Client -> Gpt3: input("Du: ")
    Gpt3 -> Gpt3: gpt3(prompt, temperature, frequency_penalty, presence_penalty, start_text, restart_text, stop_seq)
    Gpt3 -> Client: answer, prompt
    Client -> Client: print("GPT-3:" + answer)
end loop

