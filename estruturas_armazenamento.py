import numpy as np


def lista_adjacencia(grafo, v1, v2):
    grafo.vertices[v1].lista_adjacencia = np.append(grafo.vertices[v1].lista_adjacencia, v2)
    if not grafo.direcionado:
        grafo.vertices[v2].lista_adjacencia = np.append(grafo.vertices[v2].lista_adjacencia, v1)


def matriz(grafo, v1, v2):
    grafo.matriz[v1][v2] = 1
    if not grafo.direcionado:
        grafo.matriz[v2][v1] = 1
