```
sequenceDiagram
    participant TestDateien
    participant models.dateien
    participant os
    participant file
    
    TestDateien ->>+ models.dateien: schreibe_protokol(datei_namen, inhalt_einfuegen)
    models.dateien ->> os: os.path.exists(datei_namen)
    os -->> models.dateien: True
    models.dateien ->> file: open(datei_namen, "r", encoding="utf-8")
    file -->> models.dateien: file object
    models.dateien ->> file: file.read()
    file -->> models.dateien: inhalt_einfuegen
    models.dateien ->> TestDateien: self.assertEqual(file.read(), inhalt_einfuegen)
    TestDateien ->>+ models.dateien: lese_datei(datei_namen)
    models.dateien ->> file: open(datei_namen, "r", encoding="utf-8")
    file -->> models.dateien: file object
    models.dateien ->> file: file.read()
    file -->> models.dateien: inhalt_einfuegen
    models.dateien ->> TestDateien: self.assertEqual(datei_inhalt, inhalt_einfuegen)
    TestDateien ->>+ os: os.remove(datei_namen)
    os -->> TestDateien: 

