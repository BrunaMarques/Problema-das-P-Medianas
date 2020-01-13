import heapq


class vertice:
    def __init__(self, peso, capacidade, mediana):  # construtor
        self.peso = peso
        self.capacidade = capacidade
        self.mediada = false


grafo = []


def montar_grafo():
    for i in range(num_vertices):
        ver = vertice(peso, capacidade, false)
        grafo.append(ver)
