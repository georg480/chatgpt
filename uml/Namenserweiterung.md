```mermaid
sequenceDiagram
participant Benutzer
participant System
Benutzer->>System: Erweiterung des aktuellen Namensraums für Änderungen (Issues)
System-->>Benutzer: Bestätigung
Benutzer->>System: Der aktuelle Namensbereich befindet sich unter "models/namensvorgabe.py".
Benutzer->>System: Wenn etwas im Namensraum fehlt, muss es im entsprechenden Baustein ergänzt und gegebenenfalls in allen anderen ersetzt werden, bevor es verwendet wird. Es sollten deutsche Worte und Beschreibungen verwendet werden, z.B. "sende_email_an_benutzer". Zuerst wird beschrieben, was gemacht wird (z.B. "senden erstellen"), dann an wen. Es müssen nicht alle verwendeten Begriffe in der Liste aufgeführt werden, aber der Text sollte leicht verständlich sein und keine ähnlichen Begriffe enthalten.
System-->>Benutzer: Anpassung der Dokumentation und Ablaufpläne
System-->>Benutzer: Anpassung von Readme und Projektbeschreibung
Benutzer->>System: Issues abgeschlossen.
