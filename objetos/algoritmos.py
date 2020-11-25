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
        for vertice in self.grafo.vertices:
            vertice.cor = "Branco"
        self.tempo = 0
        for vertice in self.grafo.vertices:
            if vertice.cor == "Branco":
                self.visita_vertice(vertice)
