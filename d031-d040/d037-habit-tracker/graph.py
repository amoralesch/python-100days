class Graph:
    def __init__(self, id: str, name: str, unit: str, graph_type: str, color: str):
        self.id = id
        self.name = name
        self.unit = unit
        self.graph_type = graph_type
        self.color = color

    def to_dict(self) -> dict:
        return {
            'id' : self.id,
            'name' : self.name,
            'unit': self.unit,
            'type': self.graph_type,
            'color': self.color
        }
