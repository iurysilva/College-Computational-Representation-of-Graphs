class Aresta:
    def __init__(self, vertice_1, vertice_2, peso=0):
        self.v1 = vertice_1
        self.v2 = vertice_2
        self.peso = peso

    def __repr__(self):
        return str(self.v2)
