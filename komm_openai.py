import os

import openai

openai.organization = os.getenv("OPENAI_API_ORG_KEY")
openai.api_key = os.getenv("OPENAI_API_KEY")
openai.Model.list()

print(list)

import os

import openai

openai.api_key = os.getenv("OPENAI_API_KEY")
openai.Model.retrieve("text-davinci-003")


import os

import openai

openai.api_key = os.getenv("OPENAI_API_KEY")
antwort = openai.Completion.create(
    model="davinci", prompt="Say this is a test", max_tokens=7, temperature=0
)
print(antwort)

#
#
# import os
# import openai
#
# openai.api_key = "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"
#
# response = openai.Completion.create(
#     model="text-davinci-003",
#     prompt="",
#     temperature=0.7,
#     max_tokens=256,
#     top_p=1,
#     frequency_penalty=0,
#     presence_penalty=0
# )
