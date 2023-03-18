```mermaid
sequenceDiagram
    participant main
    participant Environment
    participant FileSystemLoader
    participant template
    participant file
    main->>+Environment: Erstelle Jinja2-Umgebung
    Environment->>+FileSystemLoader: Lade Template-Datei
    FileSystemLoader->>-Environment: Template-Datei
    main->>+template: Erhalte Template von Umgebung
    template->>-main: Template
    main->>+template: Rendere Template mit Variablen
    template->>-main: Gerendertes Template
    main->>+file: Öffne Datei zum Schreiben
    file->>-main: Geöffnete Datei
    main->>+file: Schreibe gerendertes Template in Datei
    file->>-main: Geschriebene Datei

