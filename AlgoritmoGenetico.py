import heapq
from random import randint
import math
from copy import deepcopy


class vertice:
    def __init__(self, x, y, capacidade, peso, mediana, listdistM, distM):  # construtor
        self.peso = peso
        self.capacidade = capacidade - peso
        self.capacidadeR = capacidade
        self.x = x
        self.y = y
        self.mediana = mediana
        self.listdistM = listdistM
        self.distM = distM
        self.alocado = False


class solucao:
    def __init__(self, med, fit):
        self.med = med
        self.fit = fit

    def __gt__(self, other):
        return self.fit > other.fit

    def __lt__(self, other):
        return self.fit < other.fit


def montaVertice(lista):
    listaVertice = []
    for i in range(len(lista)):
        v = vertice(int(lista[i][0]), int(lista[i][1]),
                    int(lista[i][2]), int(lista[i][3]), False, None, None)
        listaVertice.append(deepcopy(v))
    return listaVertice


def gerarMedianas(lista):
    medianas = []
    result = []
    while True:
        r = randint(0, numVertices-1)
        if r not in result:
            medianas.append(deepcopy(lista[r]))
            lista[r].mediana = True
            result.append(r)
        if len(result) == numMedianas:
            break

    return medianas


def distanciaMediana(listaV, listaM):
    distancia = ()
    aux = []
    for i in range(len(listaV)):
        if listaV[i].mediana != True:
            for j in range(len(listaM)):
                distancia = ((math.sqrt(
                    (listaV[i].x-listaM[j].x)**2 + (listaV[i].y-listaM[j].y)**2)), j)
                aux.append(deepcopy(distancia))

            listaV[i].listdistM = sorted(aux)
            #print('\n\ni = ', i, 'distM = ', listaV[i].distM)
        distancia = []
        aux = []


def conectaVertices(listaV, listaM):
    dic = {}
    distanciaMediana(listaV, listaM)
    for j in range(len(listaM)):
        v = []
        for i in range(len(listaV)):
            if listaV[i].mediana == True:
                continue
            elif listaM[j].capacidade < listaV[i].peso:
                continue
            elif listaV[i].alocado == False:
                for k in range(len(listaV[i].listdistM)):
                    if listaV[i].listdistM[k][1] == j:
                        listaM[j].capacidade = listaM[j].capacidade - \
                            listaV[i].peso
                        v.append(i)
                        listaV[i].alocado = True
                        listaV[i].distM = deepcopy(listaV[i].listdistM[k][0])
        dic[j] = deepcopy(v)

    return dic


def fitness(dic, lista):
    soma = 0
    for i in dic:
        for j in dic[i]:
            soma += lista[j].distM
    return soma


def gerarPopulacao():
    n = 0
    s = solucao(None, None)
    listaSolucao = []

    while (n < 100):
        dic = {}
        listaVertices = deepcopy(montaVertice(listaEntrada))
        listaMed = deepcopy(gerarMedianas(listaVertices))
        s.med = (deepcopy(listaMed))
        dic = deepcopy(conectaVertices(listaVertices, listaMed))
        s.fit = (deepcopy(fitness(dic, listaVertices)))
        listaSolucao.append(deepcopy(s))

        n += 1
    return listaSolucao


def selecao(listaSol):
    k = 5
    i = 0
    result = []
    torneio = []
    while True:
        r = randint(0, len(listaSol)-1)
        if r not in result:
            result.append(r)
            torneio.append(deepcopy(listaSol[r]))
        if len(result) == k:
            break

    geradores = []
    geradores = sorted(torneio)
    for i in range(5):
        print(geradores[i].fit)
    pai = geradores[0]
    mae = geradores[1]

    print(pai.fit)
    print(mae.fit)


listaEntrada = []
entrada = input().split()
numVertices = int(entrada[0])
numMedianas = int(entrada[1])
for i in range(numVertices):
    listaEntrada.append(input().split())

selecao(gerarPopulacao())


# for i in (listaVertices):
#     print("AAAAAAA")
#     print(i.idM)
#     print('\n')
