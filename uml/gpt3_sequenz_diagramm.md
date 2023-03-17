# UML Sequenzdiagramm - gpt3.py

Das Sequenzdiagramm zeigt, wie die `gpt3`-Funktion des `gpt3.py`-Moduls von OpenAI verwendet wird, um eine Antwort auf eine Eingabeaufforderung von GPT-3 zu erhalten.

## Benutzer -> gpt3.py: Aufruf der `gpt3`-Funktion
Der Benutzer ruft die `gpt3`-Funktion auf und übergibt folgende Parameter:
- `prompt`: Die Eingabeaufforderung für GPT-3
- `engine`: Der GPT-3-Engine-Typ, der verwendet werden soll (Standardwert ist "davinci")
- `max_laenge`: Die maximale Anzahl von Tokens, die GPT-3 generieren soll (Standardwert ist 2035)
- `temperature`: Die Temperatur für die Generierung von Text (Standardwert ist 0,7)
- `top_p`: Der Top-p-Wert für die Generierung von Text (Standardwert ist 1)
- `frequency_penalty`: Die Strafe für häufig auftretende Tokens (Standardwert ist 0)
- `presence_penalty`: Die Strafe für Tokens, die in der Eingabeaufforderung bereits vorhanden sind (Standardwert ist 0)
- `start_text`: Der Text, mit dem die Generierung von Text begonnen werden soll (Standardwert ist eine leere Zeichenfolge)
- `restart_text`: Der Text, mit dem die Generierung von Text nach der Antwort von GPT-3 fortgesetzt werden soll (Standardwert ist eine leere Zeichenfolge)
- `stop_seq`: Die Sequenz von Tokens, die das Ende der Generierung von Text signalisieren (Standardwert ist ['"""'])

## gpt3.py -> OpenAI: Anfrage senden
`gpt3.py` sendet eine Anfrage an die OpenAI API, um die Eingabeaufforderung zu verarbeiten und eine Antwort von GPT-3 zu erhalten. Die Anfrage enthält folgende Informationen:
- `prompt + start_text`: Die Eingabeaufforderung mit dem Starttext, mit dem die Generierung von Text beginnt
- `engine`: Der GPT-3-Engine-Typ, der verwendet werden soll
- `max_laenge`: Die maximale Anzahl von Tokens, die GPT-3 generieren soll
- `temperature`: Die Temperatur für die Generierung von Text
- `top_p`: Der Top-p-Wert für die Generierung von Text
- `frequency_penalty`: Die Strafe für häufig auftretende Tokens
- `presence_penalty`: Die Strafe für Tokens, die in der Eingabeaufforderung bereits vorhanden sind
- `stop_seq`: Die Sequenz von Tokens, die das Ende der Generierung von Text signalisieren

## OpenAI -> gpt3.py: Antwort empfangen
OpenAI verarbeitet die Anfrage und sendet die Antwort an `gpt3.py` zurück. Die Antwort enthält folgende Informationen:
- `answer`: Die Antwort von GPT-3 auf die Eingabeaufforderung
- `new_prompt`: Die Eingabeaufforderung mit dem Starttext und der Antwort von GPT-3, die als neue Eingabeaufforderung für die näch

