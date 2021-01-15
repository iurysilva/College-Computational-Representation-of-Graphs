from estruturas.vertice import Vertice
from estruturas.aresta import Aresta
import numpy as np


class Grafo:
    def __init__(self, num_vertices, direcionado, vertice_inicial):
        self.direcionado = direcionado
        self.num_vertices = num_vertices
        self.vertices = []
        self.matriz = np.zeros((num_vertices, num_vertices), dtype="int")
        self.tempo = 0
        self.vertice_inicial = None

    def cria_vertices(self):
        self.vertices = []
        for vertice in range(self.num_vertices):
            self.vertices.append(Vertice(vertice))

    def cria_matriz(self):
        self.matriz = np.zeros((self.num_vertices, self.num_vertices), dtype="int")

    def adiciona_aresta(self, v1, v2):
        if v1 >= self.num_vertices or v2 >= self.num_vertices:
            print("Entrada inválida, vértice %d ou %d não existe" % (v1, v2))
            return 0
        aresta1 = Aresta(v1, v2)
        self.vertices[v1].lista_adjacencia.append(aresta1)
        self.matriz[v1][v2] = 1
        if not self.direcionado:
            aresta2 = Aresta(v2, v1)
            self.vertices[v2].lista_adjacencia.append(aresta2)
            self.matriz[v2][v1] = 1

    def classifica_aresta(self, aresta):
        if self.vertices[aresta.v2].cor == "Branco":
            aresta.classificacao = "Árvore"
        elif self.vertices[aresta.v2].cor == "Cinza":
            aresta.classificacao = "Retorno"
        else:
            if self.vertices[aresta.v1].tempo_descoberta < self.vertices[aresta.v2].tempo_descoberta:
                aresta.classificacao = "Avanço"
            else:
                aresta.classificacao = "Cruzamento"

    def get_lista_adjacencia(self):
        for vertice in range(self.num_vertices):
            print("lista do vertice %i: " % vertice, self.vertices[vertice].lista_adjacencia)

    def get_classificacao_arestas(self):
        print('\nclassificação das arestas do grafo:')
        for vertice in self.vertices:
            for aresta in vertice.lista_adjacencia:
                print("classificacao da aresta %d para %d: %s" % (aresta.v1, aresta.v2, aresta.classificacao))
