```mermaid
sequenceDiagram
    participant os
    participant subprocess
    participant pytest
    participant pylint
    participant isort
    participant black
    participant pyreverse
    participant pruefe_py_gebaut
    participant skript_name

    activate pruefe_py_gebaut
    pruefe_py_gebaut->>+os: getcwd()
    os-->>-pruefe_py_gebaut: Pfad zurückgeben
    pruefe_py_gebaut->>+subprocess: call("isort .", shell=True)
    subprocess-->>-pruefe_py_gebaut: returncode
    pruefe_py_gebaut->>+subprocess: call("black .", shell=True)
    subprocess-->>-pruefe_py_gebaut: returncode
    pruefe_py_gebaut->>+subprocess: call("pylint " + skript_name, shell=True)
    subprocess-->>-pruefe_py_gebaut: returncode
    pruefe_py_gebaut->>+subprocess: call("pyreverse -a1 -s1  -f ALL -d ALL  .  -o pdf", shell=True)
    subprocess-->>-pruefe_py_gebaut: returncode
    pruefe_py_gebaut->>+pytest: pytest()
    pytest-->>-pruefe_py_gebaut: returncode
    deactivate pruefe_py_gebaut

