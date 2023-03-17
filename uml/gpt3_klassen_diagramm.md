```markdown
# gpt3.py

| Class        | openai.Completion |
| ------------ | ----------------- |
| Attributes   | - prompt: str<br>- engine: str<br>- max_tokens: int<br>- temperature: float<br>- top_p: float<br>- frequency_penalty: float<br>- presence_penalty: float<br>- stop: List[str]<br>- n: int |
| Methods      | + create() |

| Function    | gpt3() |
| ----------- | ------- |
| Parameters  | - prompt: str<br>- engine: str = "davinci"<br>- max_laenge: int = 2035<br>- temperature: float = 0.7<br>- top_p: float = 1<br>- frequency_penalty: float = 0<br>- presence_penalty: float = 0<br>- start_text: str = ""<br>- restart_text: str = ""<br>- stop_seq: List[str] = ['"""'] |
| Returns     | answer: str, new_prompt: str |

