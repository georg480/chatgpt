```markdown
## Class Diagram

|TestChatGPT|
|---|
|+ test_chat_gpt_chat()|

|revChatGPT.Chatbot|
|---|
|+ config|
|+ conversation_id|
|+ parent_id|
|+ ask()|

|MagicMock|
|---|
|+ return_value|

TestChatGPT --|> revChatGPT.Chatbot
revChatGPT.Chatbot --> MagicMock

