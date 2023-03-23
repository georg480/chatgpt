```mermaid
sequenceDiagram
    participant unittest
    participant gpt3
    participant OpenAI
    participant API_Key
    unittest ->>+ gpt3: prompt = "This is a test prompt."
    activate gpt3
    gpt3 ->>+ OpenAI: API_Key, prompt
    OpenAI -->>- gpt3: response
    deactivate gpt3
    gpt3 ->>+ unittest: answer, new_prompt = response
    activate unittest
    unittest -->>- gpt3: assertIsInstance(answer, str)
    unittest -->>- gpt3: assertGreater(len(answer.strip()), 0)
    unittest -->>- gpt3: assertEqual(prompt + answer, new_prompt)
    deactivate unittest

