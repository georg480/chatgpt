```mermaid
classDiagram
    class subprocess {
        +call(command: str, **kwargs) -> CompletedProcess
    }
    class functions {
        +pruefe_py_gebaut(skript_name: str)
    }
    
    class CompletedProcess {
        -args: Tuple
        -returncode: int
        -stdout: bytes
        -stderr: bytes
        +check_returncode()
        +__str__() -> str
    }

    subprocess --|> CompletedProcess
    functions --> subprocess

