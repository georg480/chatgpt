```mermaid
sequenceDiagram
    participant mock_subprocess_call
    participant pruefe_py_gebaut
    participant mock_input
    participant eingabe
    participant unittest

    unittest ->>+ pruefe_py_gebaut: test_pruefe_py_gebaut
    pruefe_py_gebaut ->>+ mock_subprocess_call: subprocess.call
    unittest ->>+ eingabe: test_eingabe
    eingabe ->>+ mock_input: builtins.input
    mock_input -->>- eingabe: Testeingabe
    unittest ->>+ eingabe: test_eingabe_leer
    eingabe ->>+ mock_input: builtins.input
    mock_input -->>- eingabe: ""
    eingabe ->>+ mock_input: builtins.input
    mock_input -->>- eingabe: Testeingabe

