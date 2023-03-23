```mermaid
sequenceDiagram
    participant TestMyFunction
    participant my_function
    TestMyFunction->>my_function: my_function(2)
    my_function->>my_function: check type of input
    my_function->>my_function: square the input
    my_function->>TestMyFunction: return result (4)
    TestMyFunction->>my_function: my_function(3)
    my_function->>my_function: check type of input
    my_function->>my_function: square the input
    my_function->>TestMyFunction: return result (9)
    TestMyFunction->>my_function: my_function("a")
    my_function->>my_function: raise TypeError
    my_function-x TestMyFunction: TypeError

