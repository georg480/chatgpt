```
@startuml
actor User
participant gpt3
participant openai

User -> gpt3: prompt, engine, max_laenge, temperature, top_p, frequency_penalty, presence_penalty, start_text, restart_text, stop_seq
activate gpt3
gpt3 -> openai: Completion.create(prompt + start_text, engine, max_tokens, temperature, top_p, frequency_penalty, presence_penalty, stop)
activate openai
openai --> gpt3: response
deactivate openai
gpt3 -> response.choices[0]: text
activate response.choices[0]
response.choices[0] --> gpt3: answer
deactivate response.choices[0]
gpt3 -> new_prompt: prompt + start_text + answer + restart_text
activate new_prompt
new_prompt --> gpt3: new_prompt
deactivate new_prompt
gpt3 --> User: answer, new_prompt
deactivate gpt3
@enduml

