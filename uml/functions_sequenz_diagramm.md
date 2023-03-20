```mermaid
sequenceDiagram
    participant User
    participant pruefe_py_gebaut
    participant subprocess
    participant pytest
    participant eingabe

    User->>+pruefe_py_gebaut: Aufruf mit Skriptnamen
    pruefe_py_gebaut->>+subprocess: isort .
    subprocess-->>-pruefe_py_gebaut: Erfolgreich
    pruefe_py_gebaut->>+subprocess: black .
    subprocess-->>-pruefe_py_gebaut: Erfolgreich
    pruefe_py_gebaut->>+subprocess: pylint
    subprocess-->>-pruefe_py_gebaut: Erfolgreich
    pruefe_py_gebaut->>+pytest: pytest
    pytest-->>-pruefe_py_gebaut: Erfolgreich
    pruefe_py_gebaut->>User: Suche nach ERROR und entferne am Ende das init, Fehler und prüfe den Import

    User->>+eingabe: Aufruf mit Anzeige
    eingabe->>User: Eingabe anzeigen
    User->>+eingabe: Leere Eingabe
    eingabe->>User: Fehlermeldung anzeigen
    User->>+eingabe: Korrekte Eingabe
    eingabe->>User: Eingabe anzeigen

