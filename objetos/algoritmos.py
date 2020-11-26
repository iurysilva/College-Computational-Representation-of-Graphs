import numpy as np


class Algoritmos:
    def __init__(self, grafo):
        self.grafo = grafo
        self.tempo = 0

    def visita_vertice(self, vertice):
        self.tempo += 1
        print("visitando vertice %s no tempo %d: " % (vertice, self.tempo))
        vertice.cor = "Cinza"
        vertice.tempo_descoberta = self.tempo
        for aresta in vertice.lista_adjacencia:
            self.grafo.classifica_aresta(aresta)
            if self.grafo.vertices[aresta.v2].cor == "Branco":
                self.grafo.vertices[aresta.v2].antecessor = aresta.v1
                self.visita_vertice(self.grafo.vertices[aresta.v2])
        vertice.cor = "Preto"
        self.tempo += 1
        vertice.tempo_finalizacao = self.tempo
        print("finalizando vertice %s no tempo %d: " % (vertice, self.tempo))

    def dfs(self):
        print("\nExecutando Algorítmo DFS")
        self.tempo = 0
        for vertice in self.grafo.vertices:
            vertice.cor = "Branco"
            vertice.antecessor = None
        for vertice in self.grafo.vertices:
            if vertice.cor == "Branco":
                self.visita_vertice(vertice)

    def bfs(self, vertice_inicial):
        print("\nExecutando Algorítmo DFS")
        if vertice_inicial > self.grafo.num_vertices-1 or vertice_inicial < 0:
            print("Vertice inicial inválido")
            return None
        vertice_inicial = self.grafo.vertices[vertice_inicial]
        for vertice in self.grafo.vertices:
            vertice.cor = "Branco"
            vertice.antecessor = None
            vertice.distancia = -1
        vertice_inicial.cor = "Cinza"
        vertice_inicial.distancia = 0
        vertice_inicial.antecessor = None
        fila = np.array([vertice_inicial.nome])
        tamanho_fila = 1
        while tamanho_fila != 0:
            vertice = self.grafo.vertices[fila[0]]
            fila = np.delete(fila, 0)
            tamanho_fila -= 1
            print("Visitando vertice %d, fila:   " % vertice.nome, fila)
            for aresta in vertice.lista_adjacencia:
                vertice_2 = self.grafo.vertices[aresta.v2]
                if vertice_2.cor == "Branco":
                    vertice_2.cor = "Cinza"
                    vertice_2.distancia = vertice.distancia+1
                    vertice_2.antecessor = vertice_2.nome
                    fila = np.append(fila, vertice_2.nome)
                    tamanho_fila += 1
            vertice.cor = "Preto"
            print("Fila após visitar vertice %d: " % vertice.nome, fila)
