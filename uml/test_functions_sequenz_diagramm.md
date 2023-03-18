```mermaid
sequenceDiagram
    participant TestFunctions
    participant subprocess
    participant os
    participant pruefe_py_gebaut
    participant getcwd
    participant pylint
    participant pytest
    TestFunctions->>+pruefe_py_gebaut: call pruefe_py_gebaut(skript_name)
    pruefe_py_gebaut->>+os: getcwd()
    os-->>-pruefe_py_gebaut: return current working directory
    pruefe_py_gebaut->>-os: patch object getcwd
    pruefe_py_gebaut->>+subprocess: call("isort .", shell=True)
    subprocess-->>-pruefe_py_gebaut: return call status
    pruefe_py_gebaut->>+subprocess: call("black .", shell=True)
    subprocess-->>-pruefe_py_gebaut: return call status
    pruefe_py_gebaut->>+pylint: call("pylint " + skript_name, shell=True)
    pylint-->>-pruefe_py_gebaut: return pylint status
    pruefe_py_gebaut->>+subprocess: call("pytest", shell=True)
    subprocess-->>-pruefe_py_gebaut: return call status

