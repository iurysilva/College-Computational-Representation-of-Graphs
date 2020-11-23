import numpy as np


class Vertice:
    def __init__(self, nome):
        self.nome = nome
        self.lista_adjacencia = np.array([])
        self.dado = 0
        self.cor = None
        self.tempo_descoberta = None
        self.tempo_finalizacao = None
        self.antecessor = None

    def __repr__(self):
        return str(self.nome)
