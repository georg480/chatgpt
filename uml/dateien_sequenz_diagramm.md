```mermaid
sequenceDiagram
    participant User
    participant Filesystem
    participant PythonCode
    
    User->>+PythonCode: schreibe_protokol(datei_namen, inhalt_einfuegen)
    activate PythonCode
    PythonCode->>Filesystem: open(datei_namen, "a", encoding="utf-8")
    activate Filesystem
    Filesystem-->>PythonCode: file object
    PythonCode->>file object: write(inhalt_einfuegen)
    deactivate Filesystem
    PythonCode-->>User: None
    deactivate PythonCode
    
    User->>+PythonCode: lese_datei(datei_namen)
    activate PythonCode
    PythonCode->>Filesystem: open(datei_namen, "r", encoding="utf-8")
    activate Filesystem
    Filesystem-->>PythonCode: file object
    PythonCode->>file object: readlines()
    Filesystem-->>PythonCode: file content
    PythonCode->>+Filesystem: flush()
    activate Filesystem
    Filesystem-->>PythonCode: None
    deactivate Filesystem
    PythonCode-->>User: datei_inhalt
    deactivate PythonCode
    
    User->>+PythonCode: schreibe_md(datei_namen, datei_inhalt)
    activate PythonCode
    PythonCode->>Filesystem: open(datei_namen, "w", encoding="utf-8")
    activate Filesystem
    Filesystem-->>PythonCode: file object
    PythonCode->>file object: write(datei_inhalt)
    deactivate Filesystem
    PythonCode-->>User: None
    deactivate PythonCode
    
    User->>+PythonCode: schreibe_datei(datei_namen, inhalt_einfuegen)
    activate PythonCode
    PythonCode->>Filesystem: open(datei_namen, "w", encoding="utf-8")
    activate Filesystem
    Filesystem-->>PythonCode: file object
    PythonCode->>file object: write(inhalt_einfuegen)
    deactivate Filesystem
    PythonCode-->>User: None
    deactivate PythonCode
    
    User->>+PythonCode: lese_gesuchte_dateinamen(suchfilter)
    activate PythonCode
    PythonCode->>glob: glob(suchfilter, recursive=True)
    activate glob
    glob-->>PythonCode: liste mit dateinamen
    deactivate glob
    PythonCode-->>User: liste mit dateinamen
    deactivate PythonCode
    
    User->>+PythonCode: aendere_datei_pfard(datei)
    activate PythonCode
    PythonCode->>str: replace("\\", "/")
    activate str
    str-->>PythonCode: neuer dateipfad
    deactivate str
    PythonCode-->>User: neuer dateipfad
    deactivate PythonCode
    
    User->>+PythonCode: gebe_nur_dateinamen(datei_namen)
    activate PythonCode
    PythonCode->>str: split("/")
    activate str
    str-->>PythonCode: liste mit pfadteilen
    deactivate str
    PythonCode->>str: [-1]
    activate str
    str-->>PythonCode: dateiname
    deactivate str
    PythonCode-->>User: dateiname
    deactivate PythonCode

