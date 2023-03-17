```mermaid
sequenceDiagram
    participant TestDateien
    participant tempfile
    participant os
    participant models.dateien
    TestDateien->>+tempfile: mkdtemp()
    activate tempfile
    tempfile-->>-TestDateien: temp_dir
    TestDateien->>+os: os.path.join(temp_dir, "test.txt")
    activate os
    os-->>-TestDateien: test_file
    TestDateien->>+models.dateien: schreibe_protokol(test_file, "Test Protokoll")
    activate models.dateien
    models.dateien->>+models.dateien: Öffne test_file zum Schreiben
    models.dateien->>+models.dateien: Schreibe "Test Protokoll" in test_file
    models.dateien-->>-TestDateien: -
    deactivate models.dateien
    TestDateien->>+os: os.remove(test_file)
    os-->>-TestDateien: -
    TestDateien->>+os: os.rmdir(temp_dir)
    os-->>-TestDateien: -
    TestDateien->>+os: os.path.join(temp_dir, "test.txt")
    activate os
    os-->>-TestDateien: test_file
    TestDateien->>+models.dateien: lese_datei(test_file)
    activate models.dateien
    models.dateien->>+models.dateien: Öffne test_file zum Lesen
    models.dateien-->>-TestDateien: "Testinhalt zweite Zeile"
    deactivate models.dateien
    TestDateien->>+os: os.path.join(temp_dir, "test.txt")
    activate os
    os-->>-TestDateien: test_file
    TestDateien->>+models.dateien: schreibe_datei(test_file, "Testinhalt")
    activate models.dateien
    models.dateien->>+models.dateien: Öffne test_file zum Schreiben
    models.dateien->>+models.dateien: Schreibe "Testinhalt" in test_file
    models.dateien-->>-TestDateien: -
    deactivate models.dateien
    TestDateien->>+os: os.path.join(temp_dir, "test.txt")
    activate os
    os-->>-TestDateien: test_file
    TestDateien->>-os: -

