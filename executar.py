from objetos import Grafo, Algoritmos

num_vertices = 8
direcionado = True

# Criando Grafo
grafo = Grafo(num_vertices, direcionado)
grafo.cria_vertices()
grafo.adiciona_aresta(0, 2)
grafo.adiciona_aresta(0, 4)
grafo.adiciona_aresta(1, 3)
grafo.adiciona_aresta(2, 7)
grafo.adiciona_aresta(3, 6)
grafo.adiciona_aresta(4, 5)
grafo.adiciona_aresta(4, 7)
grafo.adiciona_aresta(5, 1)
grafo.adiciona_aresta(5, 4)
grafo.adiciona_aresta(5, 7)
grafo.adiciona_aresta(6, 0)
grafo.adiciona_aresta(6, 2)
grafo.adiciona_aresta(6, 4)
grafo.adiciona_aresta(7, 3)
grafo.adiciona_aresta(7, 5)
# executando DFS
algoritmos = Algoritmos(grafo)
algoritmos.dfs()
# mostrando classificação das arestas
grafo.get_classificacao_arestas()
