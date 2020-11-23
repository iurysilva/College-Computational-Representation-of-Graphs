from objetos.vertice import Vertice
from objetos.aresta import Aresta
import numpy as np


class Grafo:
    def __init__(self, num_vertices, direcionado):
        self.direcionado = direcionado
        self.num_vertices = num_vertices
        self.vertices = np.array([])
        self.matriz = np.zeros((num_vertices, num_vertices), dtype="int")
        self.tempo = 0

    def cria_vertices(self):
        for vertice in range(self.num_vertices):
            self.vertices = np.append(self.vertices, Vertice(vertice))

    def adiciona_aresta(self, v1, v2):
        if v1 >= self.num_vertices or v2 >= self.num_vertices:
            print("Entrada inválida, vértice %d ou %d não existe" % (v1, v2))
            return 0
        aresta1 = Aresta(v1, v2)
        self.vertices[v1].lista_adjacencia = np.append(self.vertices[v1].lista_adjacencia, aresta1)
        self.matriz[v1][v2] = 1
        if not self.direcionado:
            aresta2 = Aresta(v2, v1)
            self.vertices[v2].lista_adjacencia = np.append(self.vertices[v2].lista_adjacencia, aresta2)
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

    def visita_vertice(self, vertice):
        self.tempo += 1
        print("visitando vertice %s no tempo %d: " % (vertice, self.tempo))
        vertice.cor = "Cinza"
        vertice.tempo_descoberta = np.copy(self.tempo)
        for aresta in vertice.lista_adjacencia:
            self.classifica_aresta(aresta)
            if self.vertices[aresta.v2].cor == "Branco":
                self.vertices[aresta.v2].antecessor = aresta.v1
                self.visita_vertice(self.vertices[aresta.v2])
        vertice.cor = "Preto"
        self.tempo += 1
        vertice.tempo_finalizacao = self.tempo
        print("finalizando vertice %s no tempo %d: " % (vertice, self.tempo))

    def dfs(self):
        print("\nExecutando Algorítmo DFS")
        for vertice in self.vertices:
            vertice.cor = "Branco"
        self.tempo = 0
        for vertice in self.vertices:
            if vertice.cor == "Branco":
                self.visita_vertice(vertice)
