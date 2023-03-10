from gpt3 import gpt3


def komm_chat():
    prompt = """Human: Erkläre alles auf Deutsch
AI: 
Human:"""
    while True:
        prompt += input("Du: ")
        answer, prompt = gpt3(
            prompt,
            temperature=0.9,
            frequency_penalty=1,
            presence_penalty=1,
            start_text="\nAI:",
            restart_text="\nHuman: ",
            stop_seq=["\nHuman:", "\n"],
        )
        print("GPT-3:" + answer)
