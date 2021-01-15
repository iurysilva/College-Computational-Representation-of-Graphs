def DAG1(grafo):
    grafo.num_vertices = 6
    grafo.cria_vertices()
    grafo.cria_matriz()
    grafo.direcionado = True
    grafo.vertice_inicial = None

    grafo.adiciona_aresta(0, 1)
    grafo.adiciona_aresta(1, 2)
    grafo.adiciona_aresta(3, 2)
    grafo.adiciona_aresta(3, 4)
    grafo.adiciona_aresta(3, 5)
    grafo.adiciona_aresta(4, 0)
    grafo.adiciona_aresta(4, 1)
    grafo.adiciona_aresta(4, 5)
    grafo.adiciona_aresta(5, 2)


def DAG2(grafo):
    grafo.num_vertices = 10
    grafo.cria_vertices()
    grafo.cria_matriz()
    grafo.direcionado = True
    grafo.vertice_inicial = None

    grafo.adiciona_aresta(0, 1)
    grafo.adiciona_aresta(0, 2)
    grafo.adiciona_aresta(0, 3)
    grafo.adiciona_aresta(0, 5)
    grafo.adiciona_aresta(1, 2)
    grafo.adiciona_aresta(2, 3)
    grafo.adiciona_aresta(2, 4)
    grafo.adiciona_aresta(4, 6)
    grafo.adiciona_aresta(5, 4)
    grafo.adiciona_aresta(5, 6)
    grafo.adiciona_aresta(6, 7)
    grafo.adiciona_aresta(6, 8)
    grafo.adiciona_aresta(7, 8)
    grafo.adiciona_aresta(9, 6)
