```
@startuml
actor User
User -> TestMyFunction: run tests
TestMyFunction -> my_function: call my_function(2)
my_function -> TestMyFunction: return 4
TestMyFunction -> User: pass test
TestMyFunction -> my_function: call my_function(3)
my_function -> TestMyFunction: return 9
TestMyFunction -> User: pass test
TestMyFunction -> my_function: call my_function("a")
my_function -> TestMyFunction: raise TypeError
TestMyFunction -> User: pass test
@enduml

