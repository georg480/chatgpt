```
@startuml
class komm_chat {
    -prompt: str
    +komm_chat()
    +run_chat()
}

class gpt3 {
    +gpt3(prompt: str, engine: str = "davinci", max_laenge: int = 2035, temperature: float = 0.7, top_p: float = 1, frequency_penalty: float = 0, presence_penalty: float = 0, start_text: str = "", restart_text: str = "", stop_seq: list = ['"""']) -> tuple[str, str]
}

class functions {
    +eingabe(text: str) -> str
}

class Mensch {
}

class AI {
}

komm_chat -> gpt3
komm_chat -> functions
komm_chat -> Mensch
komm_chat -> AI
@enduml

