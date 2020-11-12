from vertice import Vertice
from estruturas_armazenamento import *


class Grafo:
    def __init__(self, num_vertices, direcionado):
        self.direcionado = direcionado
        self.num_vertices = num_vertices
        self.vertices = False
        self.matriz = np.zeros((num_vertices, num_vertices), dtype="int")

    def cria_vertices(self):
        self.vertices = np.array([])
        for _ in range(self.num_vertices):
            self.vertices = np.append(self.vertices, Vertice())

    def adiciona_aresta(self, v1, v2):
        lista_adjacencia(self, v1, v2)
        matriz(self, v1, v2)

    def ver_lista_adjacencia(self, vertice):
        print(self.vertices[vertice].lista_adjacencia)

