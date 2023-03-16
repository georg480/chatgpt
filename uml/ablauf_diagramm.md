```flow
st=>start: Start
op1=>operation: Lade Konfiguration
op2=>operation: Initialisiere Chatbot
op3=>operation: Erzeuge Unittest
op4=>operation: Schreibe Unittest in Datei
op5=>operation: Prüfe, ob Test erfolgreich
op6=>operation: Schreibe Anfrage an Chatbot
op7=>operation: Erhalte Antwort vom Chatbot
op8=>operation: Schreibe Antwort in Protokoll
e=>end: Ende

st->op1->op2->op3->op4->op5->op6->op7->op8->e
```