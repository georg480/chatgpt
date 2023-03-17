```mermaid
sequenceDiagram
    participant unittest
    participant models.functions
    participant os
    participant subprocess
    
    unittest->>+models.functions: test_pruefe_py_gebaut()
    activate models.functions
    models.functions->>os: os.getcwd()
    activate os
    os-->>-models.functions: path
    models.functions->>+subprocess: subprocess.call("isort .", shell=True)
    activate subprocess
    subprocess-->>-models.functions: isort result
    models.functions->>+subprocess: subprocess.call("black .", shell=True)
    subprocess-->>-models.functions: black result
    models.functions->>+subprocess: subprocess.call("pylint " + skript_name, shell=True)
    subprocess-->>-models.functions: pylint result
    models.functions->>+subprocess: subprocess.call("pyreverse -a1 -s1  -f ALL -d ALL  .  -o pdf", shell=True)
    subprocess-->>-models.functions: pyreverse result
    models.functions->>+subprocess: subprocess.call("pytest", shell=True)
    subprocess-->>-models.functions: pytest result
    deactivate subprocess
    models.functions-->>-unittest: assertion
    deactivate models.functions

