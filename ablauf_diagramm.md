```mermaid
sequenceDiagram
    participant User
    participant Programm
    User->>Programm: Programm starten
    loop
        User->>Programm: Eingabe a(abl), e(erkl.Code), f(Frage), p(prü), t(Unittest), u(E->D), x
        Programm-->>User: Prompt
        alt
            Eingabe "a"
            User->>Programm: UML Ablaufdiagramm generieren
            Programm-->>User: UML Ablaufdiagramm wird generiert
        else Eingabe "e"
            User->>Programm: Erklärung des Codes
            Programm-->>User: Erklärung des Codes wird angezeigt
        else Eingabe "f"
            User->>Programm: Eingabe Frage
            Programm-->>User: Antwort auf die Frage
        else Eingabe "p"
            User->>Programm: Skript Name
            Programm-->>User: Ausgabe, ob das Skript erfolgreich gebaut wurde oder nicht
        else Eingabe "t"
            User->>Programm: Skript Name
            Programm-->>User: Unittest wird ausgeführt
        else Eingabe "u"
            User->>Programm: Englischer Text
            Programm-->>User: Übersetzung des Textes ins Deutsche
        else Eingabe "x"
            User->>Programm: Programm beenden
            break
        end
    end
    User->>Programm: Programm beenden

