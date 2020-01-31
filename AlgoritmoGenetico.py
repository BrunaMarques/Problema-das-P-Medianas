import heapq
from random import randint
import math
from copy import deepcopy


class vertice:
    def __init__(self, x, y, capacidade, peso, listdistM, distM, alocado, idM):  # construtor
        self.peso = peso
        self.capacidadeR = capacidade
        self.capacidade = capacidade - peso
        self.x = x
        self.y = y
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
                    int(lista[i][2]), int(lista[i][3]), [], [], False, None)
        listaVertice.append(deepcopy(v))
    return listaVertice


def gerarMedianas(listaV):
    medianas = []
    result = []
    while True:
        r = randint(0, numVertices-1)
        if r not in result:
            listaV[r].idM = deepcopy(r)
            medianas.append(deepcopy(listaV[r]))

            result.append(r)
        if len(result) == numMedianas:
            break

    return medianas


def distanciaMediana(listaV, listaM):
    distancia = ()
    aux = []
    for i in range(len(listaV)):
        for j in range(len(listaM)):
            if listaV[i].idM == listaM[j].idM:
                continue
            else:
                distancia = ((math.sqrt(
                    (listaV[i].x-listaM[j].x)**2 + (listaV[i].y-listaM[j].y)**2)), j)
                aux.append(deepcopy(distancia))
            listaV[i].listdistM = sorted(aux)
        distancia = []
        aux = []


def listaPriori(listaV, listaM):
    diferenca = []
    zerar = []
    for i in range(len(listaV)):
        listaV[i].listdistM = zerar
    distanciaMediana(listaV, listaM)
    for i in range(len(listaV)):
        for j in range(len(listaM)):
            if listaV[i].idM == listaM[j].idM:
                continue
            else:
                aux = (deepcopy(listaV[i].listdistM[0]
                                [0] - listaV[i].listdistM[1][0]), i)
                diferenca.append(deepcopy(aux))
    diferenca = deepcopy(sorted(diferenca))
    return diferenca


def conectaVertices(listaV, listaM):
    diferenca = []
    fitness = 0
    diferenca = deepcopy(listaPriori(listaV, listaM))
    for j in range(len(listaM)):
        listaM[j].capacidade = deepcopy(listaM[j].capacidadeR)
    for i in range(len(listaV)):
        listaV[i].capacidade = deepcopy(listaV[i].capacidadeR)
        listaV[i].alocado = False
    for i in diferenca:
        for j in listaV[i[1]].listdistM:
            if listaV[i[1]].alocado == True:
                continue
            if listaV[i[1]].idM == listaM[j[1]].idM:
                continue
            if listaV[i[1]].peso > listaM[j[1]].capacidade:
                continue
            else:
                listaM[j[1]].capacidade = deepcopy(listaM[j[1]
                                                          ].capacidade - listaV[i[1]].peso)
                listaV[i[1]].alocado = True
                listaV[i[1]].distM = deepcopy(j[0])

                fitness = fitness + listaV[i[1]].distM
    for i in range(len(listaV)):
        for j in range(len(listaM)):
            if listaV[i].idM != listaM[j].idM:
                if listaV[i].alocado == False:
                    return False
    return fitness


def gerarPopulacao():
    n = 0
    s = solucao(None, None)
    listaSolucao = []

    while (n < calculapop):
        listaVertices = deepcopy(montaVertice(listaEntrada))
        listaMed = deepcopy(gerarMedianas(listaVertices))
        s.med = (deepcopy(listaMed))
        s.fit = deepcopy(conectaVertices(listaVertices, listaMed))
        if s.fit == False:
            continue
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
                pai.med.remove(i)  # ver
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
    aux = []
    while n < 2:
        r = randint(0, (len(filho.med)-1))
        r2 = randint(0, len(listaVertice)-1)
        if r not in result:
            result.append(deepcopy(r))
            if listaVertice[r2].idM != filho.med[r].idM:
                filho.med.remove(filho.med[r])
                listaVertice[r2].idM = r2
                filho.med.append(deepcopy(listaVertice[r2]))
                listaVertice[filho.med[r].idM].idM = None
            n += 1
    aux = deepcopy(montaVertice(listaEntrada))
    filho.fit = deepcopy(conectaVertices(aux, filho.med))
    if filho.fit == False:
        mutacao(filho)

    return filho


def steadyStated(filho):  # atualiza a população

    novalista = []
    if filho.fit < listaSolucao[len(listaSolucao)-1].fit:
        listaSolucao.remove(listaSolucao[len(listaSolucao)-1])
        listaSolucao.append(filho)

    novalista = sorted(listaSolucao)
    return novalista


def buscaLocal(filho):
    result = []
    aux = listaVertice
    i = 0
    while i < numMedianas:
        r = randint(0, (len(listaVertice)-1))
        while listaVertice[r].idM == filho.med[i].idM:
            r = randint(0, (len(listaVertice)-1))
        aux = deepcopy(montaVertice(listaEntrada))
        result.append(deepcopy(r))
        vizinho = deepcopy(filho)
        vizinho.med[i] = deepcopy(aux[r])
        vizinho.med[i].idM = deepcopy(r)
        for k in range(len(vizinho.med)):
            aux[vizinho.med[k].idM].idM = deepcopy(vizinho.med[k].idM)
        vizinho.fit = deepcopy(conectaVertices(aux, vizinho.med))
        if vizinho.fit == False:
            continue
        if vizinho.fit < filho.fit:
            filho = deepcopy(vizinho)
            vizinho = solucao([], None)
            i = 0
        else:
            i += 1
    return filho


def algoGenetico(listaS):
    n = 0
    while n < 200:
        pai, mae = selecao(listaS)
        copiaPai = deepcopy(pai)
        copiaMae = deepcopy(mae)
        filho = mutacao(cruzamento(copiaPai, copiaMae))
        filho = buscaLocal(filho)
        solucoes = steadyStated(filho)
        print(solucoes[0].fit)
        n += 1


entrada = input().split()
numVertices = int(entrada[0])
numMedianas = int(entrada[1])
calculapop = int(((17.5*(math.log(numVertices)))//2)*2)

listaEntrada = []

for i in range(numVertices):
    listaEntrada.append(input().split())

listaSolucao, listaVertice = gerarPopulacao()

algoGenetico(listaSolucao)
