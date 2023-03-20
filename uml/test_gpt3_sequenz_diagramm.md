```mermaid
sequenceDiagram
    participant TestCase
    participant gpt3
    TestCase->>+gpt3: prompt
    activate gpt3
    gpt3-->>-TestCase: answer, new_prompt
    deactivate gpt3
    alt answer is a non-empty string
        TestCase->>+TestCase: test assertions
        activate TestCase
        TestCase->>+TestCase: assertIsInstance
        TestCase->>+TestCase: assertGreater
        TestCase->>+TestCase: assertEqual
        activate TestCase
        TestCase-->>-TestCase: test passed
        deactivate TestCase
    else answer is an empty string
        TestCase->>+TestCase: test failed
        activate TestCase
        TestCase-->>-TestCase: test failed
        deactivate TestCase
    end

