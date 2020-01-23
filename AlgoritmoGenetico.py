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
        self.idM = None


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
            lista[r].idM = deepcopy(r)
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
            # print('\n\ni = ', i, 'distM = ', listaV[i].distM)
        distancia = []
        aux = []


def listaPriori(listaV, listaM):
    diferenca = []
    distanciaMediana(listaV, listaM)
    for i in range(len(listaV)):
        if listaV[i].mediana == False:
            aux = (deepcopy(listaV[i].listdistM[0]
                            [0] - listaV[i].listdistM[1][0]), i)
            diferenca.append(deepcopy(aux))
    diferenca = deepcopy(sorted(diferenca))
    return diferenca


def conectaVertices(listaV, listaM):
    diferenca = []
    fitness = 0
    diferenca = deepcopy(listaPriori(listaV, listaM))
    for i in diferenca:
        for j in listaV[i[1]].listdistM:
            if listaV[i[1]].alocado == True:
                continue
            if listaV[i[1]].mediana == False:
                if listaV[i[1]].peso > listaM[j[1]].capacidade:
                    continue
                else:
                    listaM[j[1]].capacidade = deepcopy(listaM[j[1]
                                                              ].capacidade - listaV[i[1]].peso)
                    listaV[i[1]].alocado = True
                    listaV[i[1]].distM = deepcopy(j[0])

                    fitness = fitness + listaV[i[1]].distM
    return fitness


def gerarPopulacao():
    n = 0
    s = solucao(None, None)
    listaSolucao = []

    while (n < 100):
        listaVertices = deepcopy(montaVertice(listaEntrada))
        listaMed = deepcopy(gerarMedianas(listaVertices))
        s.med = (deepcopy(listaMed))
        s.fit = deepcopy(conectaVertices(listaVertices, listaMed))
        listaSolucao.append(deepcopy(s))

        n += 1
        listaAux = deepcopy(sorted(listaSolucao))
    return listaAux, listaVertices


def selecao(listaSol):
    k = 5
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
    return geradores[0], geradores[1]


def cruzamento(pai, mae):
    filho = solucao([], None)
    tamanho = len(pai.med)
    aux2 = []
    for i in pai.med:
        for j in mae.med:
            if i.idM == j.idM:
                aux2.append(deepcopy(i))
                filho.med = aux2
                pai.med.remove(i)
                mae.med.remove(j)
    result = []
    aux = True
    while len(filho.med) < tamanho:
        r = randint(0, len(pai.med)-1)
        if r not in result:
            if aux == True:
                result.append(r)
                filho.med.append(deepcopy(pai.med[r]))
                aux = False
            else:
                result.append(r)
                filho.med.append(deepcopy(mae.med[r]))
                aux = True
    return filho


def mutacao(filho):
    n = 0
    result = []
    print('tamanho do filho.med ', len(filho.med))
    for i in filho.med:
        print('filho', i.idM)
    while n < 2:
        r = randint(0, (len(filho.med)-1))
        r2 = randint(0, len(listaVertice)-1)
        if r not in result:
            result.append(deepcopy(r))
            print("R2", r2, 'r', r)
            if listaVertice[r2].idM != filho.med[r].idM:
                filho.med.remove(filho.med[r])
                listaVertice[r2].idM = r2
                filho.med.append(deepcopy(listaVertice[r2]))
            n += 1
    for i in filho.med:
        print
        i.capacidade = i.capacidadeR
        i.mediana = True

    return filho


def steadyStated(filho):
    aux = deepcopy(montaVertice(listaEntrada))
    filho.fit = deepcopy(conectaVertices(
        aux, filho.med))
    print('fit filho ', filho.fit)
    print('fit ultimo ', listaSolucao[len(listaSolucao)-1].fit)
    print('fit primeiro ', listaSolucao[0].fit)
<<<<<<< HEAD
=======

>>>>>>> 3b684dd81683e109b6227edb6432b3f6e81a4f43
    if filho.fit < listaSolucao[len(listaSolucao)-1].fit:
        listaSolucao.remove(listaSolucao[len(listaSolucao)-1])
        listaSolucao.append(filho)
    print('fit ultimo altualizado ', listaSolucao[len(listaSolucao)-1].fit)


listaEntrada = []
entrada = input().split()
numVertices = int(entrada[0])
numMedianas = int(entrada[1])
for i in range(numVertices):
    listaEntrada.append(input().split())


listaVertices = deepcopy(montaVertice(listaEntrada))
listaMed = deepcopy(gerarMedianas(listaVertices))
fitness = conectaVertices(listaVertices, listaMed)
# selecao(gerarPopulacao())
listaSolucao, listaVertice = gerarPopulacao()
pai, mae = selecao(listaSolucao)
copiaPai = deepcopy(pai)
copiaMae = deepcopy(mae)
filho = mutacao(cruzamento(copiaPai, copiaMae))
steadyStated(filho)
