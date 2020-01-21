import heapq
from random import randint
import math
from copy import deepcopy


class vertice:
    def __init__(self, x, y, capacidade, peso, mediana, distM, idM):  # construtor
        self.peso = peso
        self.capacidade = capacidade - peso
        self.capacidadeR = capacidade
        self.x = x
        self.y = y
        self.mediana = mediana
        self.distM = distM
        self.idM = idM
        self.alocado = False


listaEntrada = []
entrada = input().split()
numVertices = int(entrada[0])
numMedianas = int(entrada[1])
for i in range(numVertices):
    listaEntrada.append(input().split())

# print(listaEntrada)


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
    distancia = ()
    aux = []
    for i in range(len(listaV)):
        if listaV[i].mediana != True:
            for j in range(len(listaM)):
                distancia = ((math.sqrt(
                    (listaV[i].x-listaM[j].x)**2 + (listaV[i].y-listaM[j].y)**2)), j)
                aux.append(distancia)

            listaV[i].distM = sorted(aux)
            #print('\n\ni = ', i, 'distM = ', listaV[i].distM)
        distancia = []
        aux = []


def conectaVertices(listaV, listaM):
    v = []
    dic = {}
    distanciaMediana(listaV, listaM)
    for j in range(len(listaM)):
        for i in range(len(listaV)):
            if listaV[i].mediana == True:
                continue
            elif listaM[j].capacidade < listaV[i].peso:
                continue
            elif listaV[i].alocado == False:
                for k in range(len(listaV[i].distM)):
                    if listaV[i].distM[k][1] == j:
                        print("capacidade antes: ", j, listaM[j].capacidade)
                        print("peso: ", listaV[i].peso)
                        listaM[j].capacidade = listaM[j].capacidade - \
                            listaV[i].peso
                        print("capacidade depois:", j, listaM[j].capacidade)
                        v.append(i)
                        listaV[i].alocado = True
        dic[j] = v
        v = []
    print('dic', dic)


listaVertices = montaVertice(listaEntrada)
listaMedianas, posicaoMedianas = gerarMedianas(listaVertices)
distanciaMediana(listaVertices, listaMedianas)
conectaVertices(listaVertices, listaMedianas)

# for i in (listaVertices):
#     print("AAAAAAA")
#     print(i.idM)
#     print('\n')
