import subprocess

# Führe git status aus und erfasse die Ausgabe
output = subprocess.check_output(["git", "status"])

# Dekodiere die Ausgabe von Bytes zu String
output = output.decode("utf-8")

# Teile die Ausgabe in Zeilen auf
lines = output.split("\n")

# Initialisiere eine leere Liste für die Commit-Nachrichten-Zeilen
commit_message = []

# Schleife durch die Zeilen und suche nach geänderten Dateien
for line in lines:
    # Wenn die Zeile mit "modified:" beginnt, füge den Dateinamen zur Commit-Nachricht hinzu
    if line.startswith("\tmodified:"):
        # Entferne das Präfix "modified:" und entferne alle Leerzeichen
        file_name = line.replace("modified:", "").strip()
        # Füge einen Aufzählungspunkt mit dem Dateinamen zur Commit-Nachricht hinzu
        commit_message.append(f"- {file_name}")

# Verbinde die Commit-Nachrichten-Zeilen mit Zeilenumbrüchen
commit_message = "\n".join(commit_message)

# Öffne die Vorlagendatei im Anhängemodus
with open("commit_template.txt", "a") as f:
    # Schreibe die Commit-Nachricht in die Datei
    f.write(commit_message)