```mermaid
sequenceDiagram
    participant env
    participant template
    participant file
    participant output
    
    Note over env, template: Variablen definieren
    env->>+template: env.get_template("template.j2")
    Note over template: Template-Datei laden
    template->>+output: template.render(name=name, order=order, your_name=your_name)
    Note over output: Template mit Variablen rendern
    output->>+file: open("commit_template.txt", "w")
    Note over file: Datei öffnen
    file->>-output: file.write(output)
    Note over output: Inhalt in Datei schreiben
    file-->>-env: Datei schließen

