from jinja2 import Environment, FileSystemLoader

# Definieren Sie die Variablen
name = "Max Mustermann"
order = [
    {"name": "Produkt A", "quantity": 2, "price": 10},
    {"name": "Produkt B", "quantity": 1, "price": 5},
    {"name": "Produkt C", "quantity": 3, "price": 8},
]
your_name = "Ihr Name"

# Erstellen Sie die Jinja2-Umgebung und laden Sie die Template-Datei
env = Environment(loader=FileSystemLoader("."))
template = env.get_template("template.j2")

# Rendern Sie das Template mit den Variablen und speichern Sie es in einer Datei
output = template.render(name=name, order=order, your_name=your_name)
with open("commit_template.txt", "w") as file:
    file.write(output)
