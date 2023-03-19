import subprocess


def git_commit():
    subprocess.call(["git", "add", "."])

    antwort = subprocess.check_output(["git", "status"])
    antwort = antwort.decode("utf-8")
    lines = antwort.split("\n")
    commit_nachricht = []
    for line in lines:
        if line.startswith("\tmodified:"):
            datei_name = line.replace("modified:", "").strip()
            commit_nachricht.append(f"- {datei_name}")
    commit_nachricht = "\n".join(commit_nachricht)

    commit_beschreibung = "Funktion hinzufügen."
    author_info = "Georg Dahmen <georg.dahmen@gmx.de>"

    with open("commit_template.txt", "w", encoding="utf-8") as f:
        f.write(commit_nachricht + "\n\n" + commit_beschreibung)

    subprocess.call(
        ["git", "commit", "-F", "commit_template.txt", "--author=" + author_info]
    )


def git_push():
    subprocess.call(["git", "push"])
    subprocess.call(["git", "pull"])
