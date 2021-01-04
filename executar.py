from estruturas import Grafo
from algoritmos import DFS, BFS, Componentes_Conectados

num_vertices = 6
direcionado = False
vertice_inicial = 6

# Criando Grafo
grafo = Grafo(num_vertices, direcionado)
grafo.cria_vertices()
grafo.adiciona_aresta(0, 1)
grafo.adiciona_aresta(1, 1)
grafo.adiciona_aresta(1, 4)
grafo.adiciona_aresta(1, 3)
grafo.adiciona_aresta(3, 0)
grafo.adiciona_aresta(3, 4)
grafo.adiciona_aresta(4, 3)
grafo.adiciona_aresta(5, 2)

'''executar DFS:'''
# dfs = DFS(grafo)
# dfs.executar()
# grafo.get_classificacao_arestas()

'''executar BFS'''
# bfs = BFS(grafo)
# bfs.executar(vertice_inicial)

'''executar Componentes_Conectados'''
componentes = Componentes_Conectados(grafo)
componentes.executar()
componentes.ver_componentes()
