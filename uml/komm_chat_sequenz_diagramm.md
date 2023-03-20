```
@startuml
title: Kommunikations-Chatbot mit GPT-3

actor Benutzer
participant komm_chat
participant gpt3
participant functions

Benutzer -> komm_chat: start()
komm_chat -> gpt3: prompt
gpt3 -> functions: eingabe()
functions --> gpt3: Eingabe
gpt3 -> gpt3: Antwort generieren
gpt3 -> komm_chat: Antwort
komm_chat -> Benutzer: Antwort anzeigen
@enduml

