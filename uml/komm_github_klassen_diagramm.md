```markdown
# KommGithub

## Klassendiagramm
class Environment:
    + __init__(self, loader: FileSystemLoader)
    + get_template(self, template_name: str) -> Template

class FileSystemLoader:
    + __init__(self, searchpath: Union[str, List[str]])

class Template:
    + render(self, **context: Any) -> str

class File:
    - name: str
    - mode: str
    - encoding: Optional[str]
    - _io: IO[str]
    + __init__(self, name: str, mode: str, encoding: Optional[str] = None)
    + __enter__(self) -> IO[str]
    + __exit__(self, exc_type: Type[BaseException], exc_val: BaseException, exc_tb: TracebackType) -> None

class List:
    __module__ = 'builtins'
    __init__(self, /, *args, **kwargs)
    ...

class Union:
    __module__ = 'builtins'
    __args__ = ()

class Any:
    __module__ = 'builtins'
    ...

