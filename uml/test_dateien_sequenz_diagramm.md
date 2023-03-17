```mermaid
sequenceDiagram
    participant TestDateien
    participant tempfile
    participant os
    participant models.dateien
    
    TestDateien->>+tempfile: mkdtemp()
    activate tempfile
    tempfile-->>-TestDateien: /tmp/abc123
    deactivate tempfile
    
    TestDateien->>+os: os.path.join(self.test_dir, "test.txt")
    activate os
    os-->>-TestDateien: /tmp/abc123/test.txt
    deactivate os
    
    TestDateien->>+models.dateien: schreibe_protokol(self.test_file, "Test Protokoll")
    activate models.dateien
    models.dateien-->>-TestDateien: 
    deactivate models.dateien
    
    TestDateien->>+open: open(self.test_file, "r")
    activate open
    open-->>-TestDateien: file
    deactivate open
    
    TestDateien->>+file: file.read()
    activate file
    file-->>-TestDateien: content
    deactivate file
    
    TestDateien->>+TestDateien: assertEqual(content, "Test Protokoll")
    
    TestDateien->>+os: os.remove(self.test_file)
    activate os
    os-->>-TestDateien: 
    deactivate os
    
    TestDateien->>+os: os.rmdir(self.test_dir)
    activate os
    os-->>-TestDateien: 
    deactivate os
    
    TestDateien->>+open: open(self.test_file, "w")
    activate open
    open-->>-TestDateien: file
    deactivate open
    
    TestDateien->>+file: file.write("Testinhalt\\nzweite Zeile")
    activate file
    file-->>-TestDateien: 
    deactivate file
    
    TestDateien->>+models.dateien: lese_datei(self.test_file)
    activate models.dateien
    models.dateien-->>-TestDateien: content
    deactivate models.dateien
    
    TestDateien->>+TestDateien: assertEqual(content, "Testinhalt zweite Zeile")
    
    TestDateien->>+models.dateien: schreibe_datei(self.test_file, "Testinhalt")
    activate models.dateien
    models.dateien-->>-TestDateien: 
    deactivate models.dateien
    
    TestDateien->>+open: open(self.test_file, "r")
    activate open
    open-->>-TestDateien: f
    deactivate open
    
    TestDateien->>+f: f.read()
    activate f
    f-->>-TestDateien: content
    deactivate f
    
    TestDateien->>+TestDateien: assertEqual(content, "Testinhalt")

