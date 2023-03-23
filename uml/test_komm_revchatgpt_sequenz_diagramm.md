```
Title: chat_gpt_chat Sequence Diagram

participant TestChatGPT
participant patch
participant MagicMock
participant Chatbot
participant chatbot_instance

TestChatGPT->+patch: @patch("revChatGPT.Chatbot")
patch->+MagicMock: MagicMock()
patch->+Chatbot: Chatbot()
Chatbot->-chatbot_instance: return chatbot_instance
TestChatGPT->+chatbot_instance: mock_chatbot_instance
chatbot_instance->-mock_chatbot_instance: return mock_chatbot_instance
mock_chatbot_instance->+chatbot_instance: ask("Hello, GPT!", conversation_id="339e6ebd-e5f0-49f0-b54a-05f9614125b1", parent_id="a0c3abd8-b9bd-4b60-b31a-d73abf0ae7b7")
chatbot_instance->-mock_chatbot_instance: return mock_response
mock_chatbot_instance->-TestChatGPT: return [mock_response]

