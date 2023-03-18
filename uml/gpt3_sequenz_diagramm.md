```markdown
# Gpt3

## Sequenzdiagramm
participant Client
participant Gpt3

Client -> Gpt3: gpt3(prompt, engine, max_laenge, temperature, top_p, frequency_penalty, presence_penalty, start_text, restart_text, stop_seq)
Gpt3 -> OpenAI: set api key
Gpt3 -> OpenAI: create completion with prompt + start_text
OpenAI -> Gpt3: response with generated text
Gpt3 -> Client: return generated text and new prompt with start_text + generated text + restart_text

