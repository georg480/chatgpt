import subprocess

# Füge alle geänderten Dateien dem Index hinzu
subprocess.call(["git", "add", "."])

# Erfasse die geänderten Dateien und erstelle eine automatische Commit-Nachricht
output = subprocess.check_output(["git", "status"])
output = output.decode("utf-8")
lines = output.split("\n")
commit_message = []
for line in lines:
    if line.startswith("\tmodified:"):
        file_name = line.replace("modified:", "").strip()
        commit_message.append(f"- {file_name}")
commit_message = "\n".join(commit_message)

# Definiere die Commit-Beschreibung und Autor-Information
commit_description = "Add feature X and fix bug Y"
author_info = "Georg Dahmen <georg.dahmen@gmx.de>"

# Schreibe die Commit-Nachricht und die Commit-Beschreibung in die Vorlagendatei
with open("commit_template.txt", "w") as f:
    f.write(commit_message + "\n\n" + commit_description)

# Erstelle einen Commit mit der automatisch generierten Commit-Nachricht, der Commit-Beschreibung und der Autor-Information
subprocess.call(["git", "commit", "-F", "commit_template.txt", "--author=" + author_info])
