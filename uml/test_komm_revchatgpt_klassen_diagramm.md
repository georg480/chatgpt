```mermaid
classDiagram
    TestChatbot <|-- unittest.TestCase
    TestChatbot : +test_chat()
    TestChatbot : -__init__()
    TestChatbot : setUp()
    TestChatbot : tearDown()
    TestChatbot -- chatbot.Chatbot
    chatbot.Chatbot : -model
    chatbot.Chatbot : +__init__(model_name, max_length)
    chatbot.Chatbot : +generate_response(prompt)

