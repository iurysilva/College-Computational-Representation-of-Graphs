from objetos.vertice import Vertice
from objetos.aresta import Aresta
import numpy as np


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
        aresta1 = Aresta(v1, v2)
        self.vertices[v1].lista_adjacencia = np.append(self.vertices[v1].lista_adjacencia, aresta1)
        self.matriz[v1][v2] = 1
        if not self.direcionado:
            aresta2 = Aresta(v2, v1)
            self.vertices[v2].lista_adjacencia = np.append(self.vertices[v2].lista_adjacencia, aresta2)
            self.matriz[v2][v1] = 1

    def get_lista_adjacencia(self):
        for vertice in range(self.num_vertices):
            print("lista do vertice %i: " % vertice, self.vertices[vertice].lista_adjacencia)
