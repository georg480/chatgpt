```mermaid
classDiagram
    class TestFunctions {
        +test_pruefe_py_gebaut()
        -mock_subprocess_call
    }
    class subprocess {
        +call()
    }
    class os {
        +getcwd()
    }
    TestFunctions --|> subprocess
    TestFunctions --|> os

