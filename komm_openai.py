import os
import openai

openai.organization = os.getenv("OPENAI_API_ORG_KEY")
openai.api_key = os.getenv("OPENAI_API_KEY")

response = openai.Completion.create(
    model="davinci",
    prompt="test",
    temperature=0.7,
    max_tokens=2040,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0,
    stop=["\"\"\""]
)

print(response.choices[0].text)
