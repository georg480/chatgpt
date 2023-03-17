```mermaid
sequenceDiagram
    participant TestFunctions
    participant patch
    participant os
    participant subprocess
    participant pruefe_py_gebaut
    participant skript_name
    participant mock_subprocess_call

    TestFunctions ->>+ patch: @patch("subprocess.call")
    TestFunctions ->>+ os: getcwd()
    os -->>- TestFunctions: r"C:\\Users\\georg\\Seafile\\Meine Bibliothek-008100\\Dokumente\\documents\\programmieren\\PycharmProjects\\chatgpt"
    TestFunctions ->>+ pruefe_py_gebaut: pruefe_py_gebaut(skript_name)
    pruefe_py_gebaut ->>+ subprocess: isort .
    subprocess -->>- pruefe_py_gebaut
    pruefe_py_gebaut ->>+ subprocess: black .
    subprocess -->>- pruefe_py_gebaut
    pruefe_py_gebaut ->>+ subprocess: pylint skript_name
    subprocess -->>- pruefe_py_gebaut
    pruefe_py_gebaut ->>+ subprocess: pyreverse -a1 -s1  -f ALL -d ALL  .  -o pdf
    subprocess -->>- pruefe_py_gebaut
    pruefe_py_gebaut ->>+ subprocess: pytest
    subprocess -->>- pruefe_py_gebaut
    patch -->>- TestFunctions: mock_subprocess_call
    TestFunctions ->>+ mock_subprocess_call: assert_any_call("isort .", shell=True)
    TestFunctions ->>+ mock_subprocess_call: assert_any_call("black .", shell=True)
    TestFunctions ->>+ mock_subprocess_call: assert_any_call("pylint " + skript_name, shell=True)
    TestFunctions ->>+ mock_subprocess_call: assert_any_call("pyreverse -a1 -s1  -f ALL -d ALL  .  -o pdf", shell=True)
    TestFunctions ->>+ mock_subprocess_call: assert_any_call("pytest", shell=True)
    mock_subprocess_call -->>- TestFunctions

