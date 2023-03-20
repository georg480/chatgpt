```
@startuml
class gpt3 {
  -prompt: str
  -engine: str
  -max_laenge: int
  -temperature: float
  -top_p: float
  -frequency_penalty: float
  -presence_penalty: float
  -start_text: str
  -restart_text: str
  -stop_seq: list[str]

  +gpt3(prompt: str, engine: str, max_laenge: int, temperature: float, top_p: float, frequency_penalty: float, presence_penalty: float, start_text: str, restart_text: str, stop_seq: list[str])
  +generate_text() -> str
}

class openai {
  +api_key: str
  +Completion.create(prompt: str, engine: str, max_tokens: int, temperature: float, top_p: float, frequency_penalty: float, presence_penalty: float, stop: list[str]) -> Completion
}

class Completion {
  -choices: list[dict]
  +choices_text() -> list[str]
}
gpt3 -> Completion
openai --> Completion
@enduml

