from objetos.vertice import Vertice
from procedimentos.estruturas_armazenamento import *


class Grafo:
    def __init__(self, num_vertices, direcionado):
        self.direcionado = direcionado
        self.num_vertices = num_vertices
        self.vertices = np.array([])
        self.matriz = np.zeros((num_vertices, num_vertices), dtype="int")

    def cria_vertices(self):
        for _ in range(self.num_vertices):
            self.vertices = np.append(self.vertices, Vertice())

    def adiciona_aresta(self, v1, v2):
        lista_adjacencia(self, v1, v2)
        matriz(self, v1, v2)

    def get_lista_adjacencia(self):
        for vertice in range(self.num_vertices):
            print("lista do vertice %i: " % vertice)
            print(self.vertices[vertice].lista_adjacencia)
