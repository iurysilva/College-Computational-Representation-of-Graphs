from estruturas import Grafo
from algoritmos import DFS, BFS, Componentes_Conectados, Ordenacao_Topologica
from grafos import DAG1, DAG2


grafo_escolhido = DAG1

# Criando Grafo
grafo = Grafo()
grafo_escolhido(grafo)

'''executar DFS:'''
# dfs = DFS(grafo)
# dfs.executar()
# grafo.get_classificacao_arestas()

'''executar BFS'''
# bfs = BFS(grafo)
# bfs.executar(vertice_inicial)

'''executar Componentes_Conectados'''
# componentes = Componentes_Conectados(grafo)
# componentes.executar()
# componentes.ver_componentes()

'''executar ordenação topológica'''
ordenacao_topologica = Ordenacao_Topologica(grafo)
ordenacao_topologica.executar()
