```
@startuml
actor User
User -> gpt3: prompt, engine, max_laenge, temperature, top_p, frequency_penalty, presence_penalty, start_text, restart_text, stop_seq
activate gpt3
gpt3 -> openai: api_key
openai --> gpt3: bestätigung
gpt3 -> openai: Completion.create(prompt + start_text, engine, max_laenge, temperature, top_p, frequency_penalty, presence_penalty, stop_seq)
activate openai
openai --> Completion: neue Instanz
activate Completion
Completion --> openai: Antwort
destroy Completion
openai --> gpt3: Antwort
deactivate openai
gpt3 -> answer: response.choices[0]["text"]
activate answer
gpt3 -> new_prompt: prompt + start_text + answer + restart_text
activate new_prompt
gpt3 --> User: Antwort, new_prompt
deactivate gpt3
deactivate answer
deactivate new_prompt
@enduml

