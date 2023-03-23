```
sequenceDiagram
    participant TestKommChat
    participant builtins.input
    participant builtins.print
    participant GPT-3
    TestKommChat ->>+ builtins.input: Mocked user input
    builtins.input -->>- TestKommChat: "Was ist das Wetter heute?"
    TestKommChat ->>+ GPT-3: gpt3("Was ist das Wetter heute?")
    GPT-3 -->>- TestKommChat: "Das Wetter heute ist sonnig."
    TestKommChat ->>+ builtins.print: Mocked output
    builtins.print -->>- TestKommChat: "GPT-3:Das Wetter heute ist sonnig."
    TestKommChat ->>+ builtins.input: Mocked user input
    builtins.input -->>- TestKommChat: "Was ist deine Lieblingsfarbe?"
    TestKommChat ->>+ GPT-3: gpt3("Was ist deine Lieblingsfarbe?")
    GPT-3 -->>- TestKommChat: "Meine Lieblingsfarbe ist Blau."
    TestKommChat ->>+ builtins.print: Mocked output
    builtins.print -->>- TestKommChat: "GPT-3:Meine Lieblingsfarbe ist Blau."

