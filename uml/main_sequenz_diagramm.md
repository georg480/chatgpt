```mermaid
sequenceDiagram
    participant Benutzer
    participant main.py
    participant komm_chat.py
    participant komm_revchatgpt.py
    participant dateien.py
    participant functions.py

    Benutzer->>main.py: Eingabe a(abl), e(erkl.Code), f(Frage), p(prü), t(Unittest), u(E->D), x
    main.py->>dateien.py: lese_datei("englischer_text.txt")
    dateien.py->>main.py: Textinhalt
    main.py->>komm_revchatgpt.py: chat_gpt_chat(ANWEISUNG)
    komm_revchatgpt.py->>komm_revchatgpt.py: GPT-3 Textgenerierung
    komm_revchatgpt.py->>main.py: ANTWORT
    main.py->>dateien.py: schreibe_datei("deutscher_text.txt", ANTWORT)
    main.py->>main.py: UML Ablaufdiagramm erstellen und als Markdown ausgeben (erzeuge_uml())
    main.py->>komm_chat.py: Starte den Kommunikations-Chat (komm_chat())
    main.py->>komm_revchatgpt.py: Erzeuge Unittests (erzeuge_unittest())
    komm_revchatgpt.py->>komm_revchatgpt.py: Unittest-Generierung
    komm_revchatgpt.py->>main.py: ANTWORT
    main.py->>functions.py: pruefe_py_gebaut()
    main.py->>komm_revchatgpt.py: Chatbot befragen (chat_gpt_chat())
    komm_revchatgpt.py->>komm_revchatgpt.py: GPT-3 Textgenerierung
    komm_revchatgpt.py->>main.py: ANTWORT

