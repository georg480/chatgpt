```mermaid
classDiagram
    class TestMyFunction{
        +test_output()
        +test_input()
    }
    TestMyFunction --> my_function
    TestMyFunction --> unittest.TestCase

