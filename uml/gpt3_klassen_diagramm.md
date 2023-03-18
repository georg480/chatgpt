```
+--------------------------------------+
|              gpt3                    |
+--------------------------------------+
|                                      |
+--------------------------------------+
| - prompt: str                        |
| - engine: str                        |
| - max_laenge: int                     |
| - temperature: float                 |
| - top_p: int                         |
| - frequency_penalty: float           |
| - presence_penalty: float            |
| - start_text: str                    |
| - restart_text: str                  |
| - stop_seq: list[str]                |
+--------------------------------------+
| + gpt3(prompt, engine, max_laenge,   |
|         temperature, top_p,          |
|         frequency_penalty,          |
|         presence_penalty,           |
|         start_text, restart_text,   |
|         stop_seq) -> Tuple[str, str] |
+--------------------------------------+

