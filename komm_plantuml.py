import markdown

from IPython.display import display, Markdown
from plantuml import PlantUML

uml_code = """
@startuml
class Car {
  - make: str
  - model: str
  - year: int
  + start()
  + stop()
}

Car --> Engine
Car --> Wheel
Car --> Tire
@enduml
"""

plantuml = PlantUML(url='http://www.plantuml.com/plantuml/img/')
image = plantuml.processes(uml_code)
md = f"![UML Diagram]({image})"
display(Markdown(md))
