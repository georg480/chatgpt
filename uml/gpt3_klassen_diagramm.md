```markdown
# UML Klassendiagramm

Klasse: gpt3
-----------
- prompt: str
- engine: str
- max_laenge: int
- temperature: float
- top_p: int
- frequency_penalty: float
- presence_penalty: float
- start_text: str
- restart_text: str
- stop_seq: List[str]

+ __init__(self, prompt: str, engine: str, max_laenge: int, temperature: float, top_p: int, frequency_penalty: float, presence_penalty: float, start_text: str, restart_text: str, stop_seq: List[str])
+ gpt3(self) -> Tuple[str, str]


