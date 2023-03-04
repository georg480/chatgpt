import os
from random import randint

import openai
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")


def chat(anweisung, model):
    antwort = openai.Completion.create(
        model=model,
        prompt=anweisung,
        temperature=0.9,
        max_tokens=150,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0.6,
    )
    return antwort.choices[0].text


def play_random():
    num = randint(0, 10)
    if num > 5:
        return "größer"
    return "kleiner"
