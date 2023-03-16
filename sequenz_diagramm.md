```markdown
# UML Sequenzdiagramm des Gesamten prompt

Das UML Sequenzdiagramm des Gesamten prompt zeigt die Interaktionen zwischen den beteiligten Komponenten bei der Eingabeaufforderung.

## Aktoren
- Benutzer
- Anwendung

## Aktionsabläufe
1. Der Benutzer wird aufgefordert, eine Eingabe zu machen.
2. Der Benutzer gibt seine Eingabe ein und drückt die Eingabetaste.
3. Die Anwendung liest die Eingabe des Benutzers.
4. Die Anwendung überprüft die Gültigkeit der Eingabe.
5. Wenn die Eingabe gültig ist, wird sie zurückgegeben.
6. Wenn die Eingabe ungültig ist, wird eine Fehlermeldung ausgegeben und der Benutzer wird aufgefordert, es erneut zu versuchen. Schritte 2 bis 5 werden wiederholt, bis eine gültige Eingabe erfolgt ist.

## Aktionssequenz
Benutzer -> Anwendung: Eingabeaufforderung
activate Anwendung
Anwendung -> Benutzer: Eingabeaufforderung anzeigen
Benutzer -> Anwendung: Eingabe
activate Anwendung
Anwendung -> Anwendung: Eingabe lesen
Anwendung -> Anwendung: Eingabe überprüfen
Anwendung -> Benutzer: Gültige Eingabe zurückgeben oder Fehlermeldung anzeigen
deactivate Anwendung
Benutzer -> Anwendung: Eingabe wiederholen
activate Anwendung
Anwendung -> Anwendung: Eingabe lesen
Anwendung -> Anwendung: Eingabe überprüfen
Anwendung -> Benutzer: Gültige Eingabe zurückgeben oder Fehlermeldung anzeigen
deactivate Anwendung
... Wiederhole Schritte 5-6, bis eine gültige Eingabe erfolgt ist ...
Benutzer -> Anwendung: Gültige Eingabe
activate Anwendung
Anwendung -> Anwendung: Eingabe zurückgeben
deactivate Anwendung

