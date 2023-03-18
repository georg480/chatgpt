```mermaid
classDiagram
    class TestGPT3{
        +test_gpt3()
    }
    class gpt3{
        +gpt3(prompt: str) -> Tuple[str, str]
    }
    TestGPT3 --> gpt3

