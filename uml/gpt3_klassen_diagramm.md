```
@startuml
class gpt3 {
    -prompt: str
    -engine: str
    -max_laenge: int
    -temperature: float
    -top_p: int
    -frequency_penalty: int
    -presence_penalty: int
    -start_text: str
    -restart_text: str
    -stop_seq: list[str]
    +__init__(self, prompt:str, engine:str="davinci", max_laenge:int=2035, temperature:float=0.7, top_p:int=1, frequency_penalty:int=0, presence_penalty:int=0, start_text:str="", restart_text:str="", stop_seq:list[str]=['"""'])
    +gpt3(self) -> Tuple[str, str]
}
@enduml

