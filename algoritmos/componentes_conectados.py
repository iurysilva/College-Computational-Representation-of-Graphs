class Componentes_Conectados:
    def __init__(self, grafo):
        self.grafo = grafo
        self.numero_de_componentes = 0

    def ver_componentes(self):
        for componente in range(self.numero_de_componentes):
            print("Vertices no componente %d: " % componente)
            for vertice in self.grafo.vertices:
                if vertice.id == componente:
                    print(vertice)

    def conectado(self, vertice_1, vertice_2):
        if self.grafo.vertices[vertice_1].id is None or self.grafo.vertices[vertice_2].id is None:
            print("Os vertices não possuem ID")
            return None
        if self.grafo.vertices[vertice_1].id == self.grafo.vertices[vertice_2].id:
            print("Os vertices são conectados")
            return True
        else:
            print("Os vertices não são conectados")
            return False

    def dfs(self, vertice):
        vertice.marcado = True
        vertice.id = self.numero_de_componentes
        for aresta in vertice.lista_adjacencia:
            if not self.grafo.vertices[aresta.v2].marcado:
                self.dfs(self.grafo.vertices[aresta.v2])

    def executar(self):
        print("Executando algoritmo de Componentes Conectados")
        self.contador = 0
        for vertice in self.grafo.vertices:
            vertice.marcado = False
            vertice.id = None
        for vertice in self.grafo.vertices:
            if not vertice.marcado:
                self.dfs(vertice)
                self.numero_de_componentes += 1
