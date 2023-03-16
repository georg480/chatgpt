```
        +------------------+      +-------------+
        |     Prompt       |      |   Validator |
        +------------------+      +-------------+
        | -input: String   |      |             |
        | -promptMessage:  |      |             |
        |      String      |      |             |
        | -validator:      |      |             |
        |      Validator   |      |             |
        +------------------+      +-------------+
        | +setInput(input: |      | +validate(  |
        |   String): void  |      |    input:   |
        | +setPromptMessag |      |    String): |
        | e(promptMessage: |      |    boolean  |
        |   String): void  |      |             |
        | +setValidator(va |      |             |
        | lidator:         |      |             |
        |   Validator):    |      |             |
        |   void           |      |             |
        | +getInput():     |      |             |
        |   String         |      |             |
        | +getPromptMessa |      |             |
        | ge(): String     |      |             |
        | +getValidator(): |      |             |
        |   Validator      |      |             |
        | +promptUser():   |      |             |
        |   String         |      |             |
        +------------------+      +-------------+

