from gpt3 import gpt3
from models.functions import eingabe


def komm_chat():
    prompt = """Mensch: Erkläre alles auf Deutsch
AI: 
Mensch:"""
    while True:
        prompt += eingabe("Du: ")
        answer, prompt = gpt3(
            prompt,
            temperature=0.9,
            frequency_penalty=1,
            presence_penalty=1,
            start_text="\nAI:",
            restart_text="\nMensch: ",
            stop_seq=['"""'],
        )
        print("GPT-3:" + answer)
