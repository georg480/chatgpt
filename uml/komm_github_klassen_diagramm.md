```
@startuml
class GitCommands {
    + git_commit()
    + git_push()
    - commit_nachricht : str
    - commit_beschreibung : str
    - author_info : str
    - commit_template_file : str
    - add_file(file: str)
    - get_modified_files() : List[str]
}

class Subprocess {
    + call(command: List[str])
    + check_output(command: List[str]) : bytes
}

GitCommands --> Subprocess
@enduml

