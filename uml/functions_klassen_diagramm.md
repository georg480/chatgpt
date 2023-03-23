```plantuml
class Functions {
- recognizer : Recognizer
--
+ pruefe_py_gebaut(skript_name: str)
+ eingabe(anzeige: str) : str
+ aufnahme() : str
+ sprechen(text: str)
}
Functions --> Recognizer

