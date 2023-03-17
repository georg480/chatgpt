```mermaid
sequenceDiagram
    participant unittest
    participant models.functions
    participant subprocess
    participant os
    participant pytest
    participant isort
    participant black
    participant pylint
    participant pyreverse
    
    unittest->>+models.functions: test_pruefe_py_gebaut(skript_name)
    activate models.functions
    alt Skript existiert
        models.functions->>os: getcwd()
        os-->>models.functions: C:\\Users\\georg\\Seafile\\Meine Bibliothek-008100\\Dokumente\\documents\\programmieren\\PycharmProjects\\chatgpt
        models.functions->>subprocess: isort .
        subprocess-->>models.functions: 
        models.functions->>subprocess: black .
        subprocess-->>models.functions: 
        models.functions->>subprocess: pylint main.py
        subprocess-->>models.functions: 
        models.functions->>subprocess: pyreverse -a1 -s1  -f ALL -d ALL  .  -o pdf
        subprocess-->>models.functions: 
        models.functions->>subprocess: pytest
        subprocess-->>models.functions: 
        models.functions->>unittest: assert subprocess.call called with expected commands
        unittest-->>models.functions: 
    else Skript existiert nicht
        models.functions->>unittest: raise FileNotFoundError
        unittest-->>models.functions: 
    end
    deactivate models.functions

