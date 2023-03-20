```plantuml
@startuml
title GitHub Communication

participant User
participant Git
participant Terminal

User -> Terminal: Type 'python komm_github.py'
Terminal -> Git: git add .
Terminal -> Git: git status
Git -> Terminal: Returns the status of the files
Terminal -> Python: Parses the file names that have been modified
Python -> Terminal: Formats the commit message and author info
Terminal -> Git: git commit -F commit_template.txt --author=author_info
Git -> Terminal: Returns the commit ID
Terminal -> Git: git push
Terminal -> Git: git pull
Git -> Terminal: Returns the changes made by other users

@enduml

