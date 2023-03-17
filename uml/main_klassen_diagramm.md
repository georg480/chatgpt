```markdown
# Class Diagram

|                main.py                   |
|------------------------------------------|
|                 + MODEL                  |
|------------------------------------------|
|             while True:                  |
|          + eingabe_benutzer               |
|               if 'u':                     |
|                 + lese_datei()            |
|                 + ANWEISUNG               |
|                 + ANTWORT                 |
|                 + schreibe_datei()        |
|               if 'a':                     |
|                 + erzeuge_uml()           |
|               if 'c':                     |
|                 + komm_chat()             |
|               if 't':                     |
|                 + erzeuge_unittest()      |
|               if 'p':                     |
|                 + pruefe_py_gebaut()      |
|               if 'f':                     |
|                 + ANWEISUNG               |
|                 + ANTWORT                 |
|               if 'e':                     |
|                 + ANWEISUNG               |
|                 + lese_datei()            |
|                 + ANWEISUNG               |
|                 + ANTWORT                 |
|               if 'x':                     |
|                 + break                   |
|               else:                       |
|                 + eingabe_benutzer        |
|------------------------------------------|
|            komm_chat()                    |
|           + input_text                    |
|------------------------------------------|
|              chat()                       |
|         + input_text                      |
|         + model_name                      |
|         + max_length                      |
|------------------------------------------|
|            erzeuge_uml()                  |
|------------------------------------------|
|         erzeuge_unittest()                |
|           + script_name                   |
|           + model_name                    |
|------------------------------------------|
|            lese_datei()                   |
|           + dateiname                     |
|------------------------------------------|
|          schreibe_datei()                 |
|           + dateiname                     |
|           + inhalt                        |
|------------------------------------------|
|        pruefe_py_gebaut()                 |
|           + script_name                   |
|------------------------------------------|
|        + pruefe_py_gebaut()               |
|------------------------------------------|
|          + pruefe_py_gebaut()             |
|------------------------------------------|

