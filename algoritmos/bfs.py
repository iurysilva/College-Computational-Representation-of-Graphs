import numpy as np


class BFS:
    def __init__(self, grafo):
        self.grafo = grafo

    def executar(self, vertice_inicial):
        print("\nExecutando Algorítmo BFS")
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
