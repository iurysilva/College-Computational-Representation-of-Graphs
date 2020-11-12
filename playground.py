from objetos import Grafo

num_vertices = 7
direcionado = False

# Criando Grafo
grafo = Grafo(num_vertices, direcionado)
grafo.cria_vertices()
grafo.adiciona_aresta(0, 1)
grafo.adiciona_aresta(0, 2)
grafo.adiciona_aresta(0, 5)
grafo.adiciona_aresta(0, 6)
grafo.adiciona_aresta(3, 4)
grafo.adiciona_aresta(3, 5)
grafo.adiciona_aresta(4, 5)
grafo.adiciona_aresta(4, 6)

# printando listas de adjacencia e matriz do grafo
print('matriz do grafo')
print(grafo.matriz, "\n")
grafo.get_lista_adjacencia()
