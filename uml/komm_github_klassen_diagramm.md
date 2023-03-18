```markdown
@startuml
class Jinja2Environment {
    -loader: FileSystemLoader
    ..constructor..
    +get_template(name: str) -> Template
}
class FileSystemLoader {
    ..constructor..
}
class Template {
    +render(**context) -> str
}
class File {
    -name: str
    -mode: str
    -buffering: int
    -encoding: str
    -newline: str
    ..constructor..
    +write(s: str) -> int
    +__enter__() -> File
    +__exit__(exc_type, exc_val, exc_tb) -> None
}
class List {
    -items: List[Any]
    ..constructor..
    +__len__() -> int
    +__iter__() -> Iterator[Any]
}
class Dict {
    -data: Dict[KT, VT]
    ..constructor..
    +keys() -> KeysView[KT]
    +values() -> ValuesView[VT]
    +items() -> ItemsView[KT, VT]
    +__contains__(key: Any) -> bool
}
Jinja2Environment --> FileSystemLoader
Jinja2Environment --> Template
Template --> File
Template --> List
Template --> Dict
@enduml

