```mermaid
sequenceDiagram
    participant TestDateien
    participant tempfile
    participant os
    participant models.dateien
    
    TestDateien->>+tempfile: mkdtemp()
    activate tempfile
    tempfile-->>-TestDateien: /path/to/temp/dir
    
    TestDateien->>+os: path join(test_dir, "test.txt")
    activate os
    os-->>-TestDateien: /path/to/temp/dir/test.txt
    
    TestDateien->>+TestDateien: setUp()
    activate TestDateien
    TestDateien->>+models.dateien: schreibe_protokol(test_file, "Test Protokoll")
    activate models.dateien
    models.dateien->>+models.dateien: open(test_file, "w")
    models.dateien->>+models.dateien: write("Test Protokoll")
    models.dateien-->>-models.dateien: close()
    models.dateien-->>-TestDateien: 
    TestDateien->>-models.dateien: 
    TestDateien->>+os: remove(test_file)
    os-->>-TestDateien: 
    TestDateien->>+os: rmdir(test_dir)
    os-->>-TestDateien: 
    
    TestDateien->>+TestDateien: tearDown()
    activate TestDateien
    TestDateien->>+models.dateien: lese_datei(test_file)
    activate models.dateien
    models.dateien->>+models.dateien: open(test_file, "r")
    models.dateien->>+models.dateien: read()
    models.dateien-->>-models.dateien: close()
    models.dateien-->>-TestDateien: content
    TestDateien->>-models.dateien: 
    TestDateien->>+TestDateien: assertEqual(content, "Testinhalt zweite Zeile")
    
    TestDateien->>+TestDateien: test_schreibe_datei()
    activate TestDateien
    TestDateien->>+models.dateien: schreibe_datei(test_file, "Testinhalt")
    activate models.dateien
    models.dateien->>+models.dateien: open(test_file, "w")
    models.dateien->>+models.dateien: write("Testinhalt")
    models.dateien-->>-models.dateien: close()
    models.dateien-->>-TestDateien: 
    TestDateien->>-models.dateien: 
    TestDateien->>+models.dateien: open(test_file, "r")
    activate models.dateien
    models.dateien->>+models.dateien: read()
    models.dateien-->>-models.dateien: close()
    models.dateien-->>-TestDateien: content
    TestDateien->>-models.dateien: 
    TestDateien->>+TestDateien: assertEqual(content, "Testinhalt")
    

