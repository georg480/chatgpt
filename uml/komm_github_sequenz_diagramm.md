```mermaid
sequenceDiagram
    participant C as Client
    participant S as Server
    C->>+S: name = "Max Mustermann"
    C->>+S: order = [{"name": "Produkt A", "quantity": 2, "price": 10},{"name": "Produkt B", "quantity": 1, "price": 5},{"name": "Produkt C", "quantity": 3, "price": 8}]
    C->>+S: your_name = "Ihr Name"
    S->>+S: env = Environment(loader=FileSystemLoader("."))
    S->>+S: template = env.get_template("template.j2")
    S->>+S: output = template.render(name=name, order=order, your_name=your_name)
    S->>-C: Write output to commit_template.txt

