class Kruskal:
    def __init__(self, grafo):
        self.arvores = []
        self.grafo = grafo

    def cria_floresta(self):
        for vertice in self.grafo.vertices:
            vertice.id = vertice.nome
            self.arvores.append([vertice.id])

    def atualiza_ids(self, id):
        for vertice in self.arvores[id]:
            self.grafo.vertices[vertice].id = id

    def mostra_conjuntos(self):
        for conjunto in self.arvores:
            if conjunto:
                print(conjunto)

    def retorna_marcara(self):
        mascara = []
        for arvore in self.arvores:
            if arvore:
                mascara.append(arvore)
        return mascara

    def executar(self):
        peso_total = 0
        self.grafo.ordena_arestas()
        for vertice in self.grafo.vertices:
            vertice.id = vertice.nome
        self.cria_floresta()
        for aresta in self.grafo.arestas:
            vertice_1 = self.grafo.vertices[aresta.v1]
            vertice_2 = self.grafo.vertices[aresta.v2]
            if vertice_1.id != vertice_2.id:
                print('Conectando vertices %d e %d' % (vertice_1.nome, vertice_2.nome))
                nova_arvore = self.arvores[vertice_1.id] + self.arvores[vertice_2.id]
                self.arvores[vertice_1.id] = nova_arvore
                self.arvores[vertice_2.id] = []
                self.atualiza_ids(vertice_1.id)
                print('Árvores atualmente: ', self.retorna_marcara())
                peso_total = peso_total + aresta.peso
        print('peso total da árvore: ', peso_total)
