class Vertice:
    def __init__(self, nome):
        self.nome = nome
        self.lista_adjacencia = []
        self.dado = 0
        self.cor = None
        self.tempo_descoberta = None
        self.tempo_finalizacao = None
        self.antecessor = None
        self.distancia = None
        self.marcado = False
        self.id = None

    def __repr__(self):
        return str(self.nome)
