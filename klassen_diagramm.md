```mermaid
classDiagram
    class komm_chat
    class komm_revchatgpt
    class models.dateien
    class models.functions
    class main
    
    class komm_revchatgpt {
        +chat()
        +erzeuge_unittest()
        +erzeuge_uml()
    }
    
    class models.dateien {
        +lese_datei()
        +schreibe_datei()
    }
    
    class models.functions {
        +pruefe_py_gebaut()
    }
    
    class main {
        -MODEL
        +loop()
    }
    
    komm_chat --> main
    main --> komm_revchatgpt
    main --> models.dateien
    main --> models.functions
    komm_revchatgpt --> models.dateien

