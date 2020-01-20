import heapq
from random import randint
import math


class vertice:
    def __init__(self, x, y, peso, capacidade, mediana, distM, idM):  # construtor
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
                    int(lista[i][2]), int(lista[i][3]), False, None, None)
        listaVertice.append(v)
    return listaVertice


def gerarMedianas(lista):
    medianas = []
    result = []
    while True:
        r = randint(0, numVertices-1)
        if r not in result:
            medianas.append(lista[r])
            lista[r].mediana = True
            result.append(r)
        if len(result) == numMedianas:
            break

    return medianas, result


def distanciaMediana(listaV, listaM):
    distancia = []
    for i in range(numVertices):
        if listaV[i].mediana == True:
            continue
        for j in range(numMedianas):
            distancia.append(math.sqrt(
                (listaV[i].x-listaM[j].x)**2 + (listaV[i].y-listaM[j].y)**2))
            print('ITERACAO ------ ', i)
            print('Xv: ', listaV[i].x)
            print('Xm: ', listaM[j].x)
            print('Yv: ', listaV[i].y)
            print('Ym: ', listaM[j].y)
            print('Distancia: ', distancia[j])
        listaV[i].distM = min(distancia)
        listaV[i].idM = distancia.index(min(distancia))
        distancia = []
        print(listaV[i].distM)
        print(listaV[i].idM)


listaVertices = montaVertice(listaEntrada)
listaMedianas, posicaoMedianas = gerarMedianas(listaVertices)
distanciaMediana(listaVertices, listaMedianas)

# for i in range(len(listaMedianas)):
#     print("AAAAAAA")
#     print(listaMedianas[i].x)
#     print(listaMedianas[i].y)
