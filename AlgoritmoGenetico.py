import heapq
from random import randint


class vertice:
    def __init__(self, x, y, peso, capacidade, mediana):  # construtor
        self.peso = peso
        self.capacidade = capacidade
        self.x = x
        self.y = y
        self.mediada = mediana


listaEntrada = []
entrada = input().split()
numVertices = int(entrada[0])
numMedianas = int(entrada[1])
for i in range(numVertices):
    listaEntrada.append(input().split())

print(listaEntrada)


def montaVertice(lista):
    listaVertice = []
    for i in range(len(lista)):
        v = vertice(int(lista[i][0]), int(lista[i][1]),
                    int(lista[i][2]), int(lista[i][3]), False)
        listaVertice.append(v)
    return listaVertice


def gerarMedianas(lista):
    medianas = []
    for i in range(numMedianas):
        r = randint(0, len(lista))
        if r not in result:
            mediadas.append(liesta[r])


listaVestices = montaVertice(listaEntrada)
gerarMedianas(listaVestices)
