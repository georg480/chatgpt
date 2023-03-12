import os

import openai

# from transformers import AutoTokenizer
#
# gpt2_tokenizer = AutoTokenizer.from_pretrained("gpt2", use_fast=True)
openai.api_key = os.getenv("OPENAI_API_KEY")


def gpt3(
    prompt,
    engine="davinci",
    max_laenge=2035,
    temperature=0.7,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0,
    start_text="",
    restart_text="",
    stop_seq=['"""'],
):
    response = openai.Completion.create(
        prompt=prompt + start_text,
        engine=engine,
        max_tokens=max_laenge,
        temperature=temperature,
        top_p=top_p,
        frequency_penalty=frequency_penalty,
        presence_penalty=presence_penalty,
        stop=stop_seq,
    )
    answer = response.choices[0]["text"]
    new_prompt = prompt + start_text + answer + restart_text
    return answer, new_prompt
