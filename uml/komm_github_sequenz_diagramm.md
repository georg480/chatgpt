```mermaid
sequenceDiagram
    participant User
    participant subprocess
    participant Git

    User->>subprocess: call(["git", "add", "."])
    subprocess->>subprocess: check_output(["git", "status"])
    subprocess->>subprocess: decode("utf-8")
    subprocess->>subprocess: split("\n")
    loop for each line in the output
        subprocess->>subprocess: replace("modified:", "").strip()
        subprocess->>subprocess: append to commit_nachricht list
    end
    subprocess->>subprocess: join commit_nachricht list
    User->>subprocess: open("commit_template.txt", "w", encoding="utf-8")
    subprocess->>subprocess: write(commit_nachricht + "\n\n" + commit_beschreibung)
    User->>subprocess: call(["git", "commit", "-F", "commit_template.txt", "--author=" + author_info])
    User->>Git: push changes to remote repository
    Git->>subprocess: call(["git", "push"])
    Git->>subprocess: call(["git", "pull"])

