```
@startuml
class komm_chat {
    - prompt: str
    + __init__()
    + start()
}
class gpt3 {
    - prompt: str
    - engine: str
    - max_laenge: int
    - temperature: float
    - top_p: int
    - frequency_penalty: int
    - presence_penalty: int
    - start_text: str
    - restart_text: str
    - stop_seq: list[str]
    + __init__()
    + gpt3()
}
class functions {
    + eingabe()
}

komm_chat -> gpt3: Verwendung
komm_chat -> functions: Verwendung
@enduml

