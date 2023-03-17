```mermaid
sequenceDiagram
    participant User
    participant Jinja2
    participant FileSystemLoader
    participant Environment
    participant template.j2
    participant File
    
    User ->>+ FileSystemLoader: Lade Vorlagen-Datei
    FileSystemLoader ->>+ template.j2: Lade Vorlage
    User ->>+ Environment: Erstelle Jinja2-Umgebung
    Environment ->>+ template.j2: Rendern des Templates mit Variablen
    template.j2 ->>+ Environment: Rendern des Templates
    Environment ->>+ File: Öffnen der Datei "commit_template.txt"
    File ->>+ Environment: Schreiben des gerenderten Templates in die Datei
    Environment ->>- File: Schließen der Datei "commit_template.txt"
    User ->>- Environment: Erstelle commit_template.txt

