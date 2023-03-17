```mermaid
sequenceDiagram
    participant App
    participant subprocess
    App->>subprocess: call("isort .")
    subprocess-->>App: return
    App->>subprocess: call("black .")
    subprocess-->>App: return
    App->>subprocess: call("pylint " + skript_name)
    subprocess-->>App: return
    App->>subprocess: call("pyreverse -a1 -s1  -f ALL -d ALL  .  -o pdf")
    subprocess-->>App: return
    App->>subprocess: call("pytest")
    subprocess-->>App: return
    App->>App: print("Suche nach ERROR und entferne am Ende das init, Fehler und prüfe den Import")

