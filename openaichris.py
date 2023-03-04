import os

import openai
from dotenv import load_dotenv

# API_KEY = 'xxxxxxxx'

load_dotenv()
API_KEY = os.getenv("OPENAI_API_KEY")


def chat(prompt):
    completions = openai.Completion.create(
        model="text-davinci-002",
        prompt=prompt,
        max_tokens=1024,
        api_key="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",
    )
    message = completions.choices[0].text
    return message


result = chat("Schreib mir einen weihnachtlichen Text.")
print(result)
