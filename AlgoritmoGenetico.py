import heapq
from random import randint
import math


class vertice:
    def __init__(self, x, y, peso, capacidade, mediana):  # construtor
        self.peso = peso
        self.capacidade = capacidade
        self.x = x
        self.y = y
        self.mediana = mediana
        self.distM = distM
        self.idM = idM


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
    result = []
    while True:
        r = randint(0, numVertices-1)
        if r not in result:
            lista[r].capacidade = lista[r].capacidade - lista[r].peso
            medianas.append(lista[r])
            lista[r].mediana = True
            result.append(r)
        if len(result) == numMedianas:
            break

    return medianas, result


def distanciaMediana(listaV, listaM):
    distancia = tuple()
    matriz = []
    tupla = tuple()
    capacidade = 0
    dic = {}
    aux = []
    for i in range(numVertices):
        if listaV[i].mediana == True:
            continue
        for j in range(numMedianas):
            distancia = ((math.sqrt(
                (listaV[i].x-listaM[j].x)**2 + (listaV[i].y-listaM[j].y)**2)), j)
            aux.append(distancia)
        matriz.append(aux)
        distancia = []
        aux = []

    print("matriz: ", matriz)

# def conectaVertices(listaV, listaM):


listaVertices = montaVertice(listaEntrada)
listaMedianas, posicaoMedianas = gerarMedianas(listaVertices)
distanciaMediana(listaVertices, listaMedianas)

# for i in range(len(listaMedianas)):
#     print("AAAAAAA")
#     print(listaMedianas[i].x)
#     print(listaMedianas[i].y)
