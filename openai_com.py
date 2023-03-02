# import asyncio
import os

import openai
from dotenv import load_dotenv

# import shutil
# from datetime import datetime


load_dotenv()
API_KEY = os.getenv("OPENAI_API_KEY")


# def chat(prompt):
#     completions = openai.Completion.create(
#         model="text-davinci-003", prompt=prompt, max_tokens=2048, api_key=API_KEY
#     )
#     message = completions.choices[0].text
#     return message


def chat(prompt):
    completions = openai.Completion.create(
        model="text-davinci-003", prompt=prompt, max_tokens=2048, api_key=API_KEY
    )
    message = completions.choices[0].text
    return message


result = chat("Schreib mir einen weihnachtlichen Text. in deutsch")
#print(result)
