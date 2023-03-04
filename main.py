from openai_com import chat

model = "text-davinci-003"
anweisung = "Gebe Hallo Georg aus."
antwort = chat(anweisung, model)
print(f"antwort: {antwort}")
