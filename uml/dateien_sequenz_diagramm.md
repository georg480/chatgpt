```mermaid
sequenceDiagram
    participant User
    participant dateien.py
    User->>dateien.py: schreibe_protokol(datei_namen, inhalt_einfuegen)
    dateien.py->>datei_namen: open(datei_namen, "a", encoding="utf-8")
    datei_namen->>dateien.py: file
    User->>datei_inhalt: lese_datei(datei_namen)
    datei_inhalt->>dateien.py: open(datei_namen, "r", encoding="utf-8")
    dateien.py->>datei_inhalt: file
    datei_inhalt->>dateien.py: readlines()
    dateien.py->>datei_inhalt: [line.strip() for line in file.readlines()]
    dateien.py->>datei_inhalt: " ".join([line.strip() for line in file.readlines()])
    dateien.py->>file: flush()
    file->>dateien.py: schreibe_protokol(datei_namen, inhalt_einfuegen)
    dateien.py->>User: return datei_inhalt
    User->>dateien.py: schreibe_md(datei_namen, datei_inhalt)
    dateien.py->>datei_namen: open(datei_namen, "w", encoding="utf-8")
    datei_namen->>dateien.py: file
    dateien.py->>datei_inhalt: datei_inhalt[datei_inhalt.index("```") : datei_inhalt.rindex("```")]
    dateien.py->>lines: for line in lines.split("\
")
    lines->>file: write(line + "\n")
    file->>dateien.py: schreibe_md(datei_namen, datei_inhalt)
    dateien.py->>User: return
    User->>dateien.py: schreibe_datei(datei_namen, inhalt_einfuegen)
    dateien.py->>datei_namen: open(datei_namen, "w", encoding="utf-8")
    datei_namen->>dateien.py: file
    file->>dateien.py: write(inhalt_einfuegen)
    dateien.py->>User: return
    User->>dateien.py: lese_gesuchte_dateinamen(suchfilter)
    dateien.py->>glob: glob.glob(suchfilter, recursive=True)
    glob->>dateien.py: return
    dateien.py->>User: return
    User->>dateien.py: aendere_datei_pfard(datei)
    dateien.py->>datei: replace("\\", "/")
    datei->>dateien.py: return
    dateien.py->>User: return
    User->>dateien.py: gebe_nur_dateinamen(datei_namen)
    dateien.py->>datei_namen: split("/")[-1]
    datei_namen->>dateien.py: return
    dateien.py->>User: return

