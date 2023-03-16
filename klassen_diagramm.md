```mermaid
classDiagram
    class User {
        +name : string
        +sendRequest(prompt: string) : void
        +receiveResponse(response: string) : void
    }

    class Code {
        -openai : OpenAI_API
        +gpt3(prompt: string) : string
    }

    class OpenAI_API {
        -api_key : string
        +generateResponse(prompt: string) : string
    }

    User --> Code
    Code --> OpenAI_API

