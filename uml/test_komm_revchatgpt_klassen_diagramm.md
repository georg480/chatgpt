```
 +--------------------+       +------------------+
 |    TestChatGPT     |       |     Chatbot      |
 +--------------------+       +------------------+
 | - test_chat_gpt_chat(mock_chatbot) |     |                  |
 +--------------------+       | - config: dict    |
                              | - conversation_id: str |
                              | - parent_id: str   |
                              | - ask(message: str)  |
                              +------------------+
                              |     Chatbot      |
                              +------------------+

