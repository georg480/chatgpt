import os
from datetime import datetime

import openai
from dotenv import load_dotenv

from models.dateien import schreibe_protokol

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")


def chat(anweisung, model):
    zeit_aktuell = datetime.now().strftime("%Y.%m.%d_%H:%M:%S")
    schreibe_protokol("protokoll.txt", f"zu gpt {zeit_aktuell}: {anweisung}\n")
    antwort = openai.Completion.create(
        model=model,
        prompt=anweisung,
        temperature=0.9,
        max_tokens=150,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0.6,
    )
    schreibe_protokol("protokoll.txt", f"von gpt {zeit_aktuell}: {antwort}\n")
    print(f"Antwort: {antwort.choices[0].text}")
    return antwort.choices[0].text
