import networkx as nx
import numpy as np
import matplotlib.pyplot as plt

def mostraGrafo(matriz):
    b = np.matrix(matriz)
    k = nx.from_numpy_matrix(b)
    nx.draw(k,with_labels=1)
    plt.show()

def verificaAresta(matriz,a,b):
    if (matriz[a][b] == 1 ):
        return True

def grauVertice(matriz,a):
    cont = 0
    for i in range(0, vertices):
        if (matriz[i][a] == 1 or matriz[a][i] == 1):
            cont += 1
    return cont

def gerarCaminho(grafo, caminho, final):
    if caminho[-1] == final:
        yield caminho
        return
    for vizinho in dicionario[caminho[-1]]:
        if vizinho in caminho:
            continue
        for caminho_maior in gerarCaminho(grafo, caminho + [vizinho], final):
            yield caminho_maior

def ciclo(grafo, inicio, fim):
    margem = [(inicio, [])]
    while margem:
        estado, caminho = margem.pop()
        if caminho and estado == fim:
            yield caminho
            continue
        for proximoEstado in grafo[estado]:
            if proximoEstado in caminho:
                continue
            margem.append((proximoEstado, caminho+[proximoEstado]))

def matrizDicionario(matriz):
    dicionario = {}
    for i in range(0, vertices):
        dicionario[i] = []
        for j in range(0, vertices):
            if (matriz[i][j] == 1):
                dicionario[i].append(j)
    return dicionario





#=======================================================================================================================

vertices = int(input("Digite a quantidade de Vértices: "))
matriz = []
for i in range(0, vertices):
    linha = []
    for j in range(0, vertices):
        linha.append(0)
    matriz.append(linha)

while True:
    print('========================= Trabalho de Grafos =========================')
    print('1 - Mostrar grafo')
    print('2 - Adicionar arestas')
    print('3 - Verifica arestas')
    print('4 - Grau de um vértice')
    print('5 - Verifique se há caminho entre eles')
    print('6 - Verifique se há um ciclo no grafo')
    print('7 - Busca em largura')
    print('8 - Busca em profundidade')
    print('0 - Sair')
    op = int(input("Digite a opção: "))
    if(op==1):
        mostraGrafo(matriz)
    elif (op == 2):
        a = int(input('vértice A:'))
        b = int(input('vértice B:'))
        for i in range(0, vertices):
            for j in range(0, vertices):
                if ((i == a) and (j == b)):
                    matriz[i][j]=1
                    matriz[j][i] = 1
    elif (op == 3):
        a = int(input('vértice A:'))
        b = int(input('vértice B:'))
        if (verificaAresta(matriz,a,b)):
            print('Sim')
        else:
            print('Não')
    elif (op == 4):
        a = int(input('vértice:'))
        print(grauVertice(matriz,a))
    elif (op == 5):
        cam=[]
        a = int(input('vértice A:'))
        b = int(input('vértice B:'))
        dicionario = matrizDicionario(matriz)
        for caminho in gerarCaminho(dicionario, [a], b):
            cam.append(caminho)
        if caminho==[]:
            print('Não há caminho')
        else:
            print('Tem caminho!')
            for i in range(0, len(cam)):
                print(cam[i])
    elif (op == 6):
        cont =0
        dicionario = matrizDicionario(matriz)
        a = int(input('vértice:'))
        ciclos = [[node] + path for node in dicionario for path in ciclo(dicionario, a, a)]
        if ciclos==[]:
            print('Não há ciclo para esse vertice')
        else:
            for i in range(0,len(ciclos)):
                if (len(ciclos[i])>3) and (ciclos[i][0]==ciclos[i][len(ciclos[i])-1]) :
                    print(ciclos[i])
                    cont = 1
            if cont==0:
                print('Não há ciclo para esse vertice')
    elif (op == 7):
        a = int(input('vértice:'))
    elif (op == 8):
        a = int(input('vértice:'))
        dicionario = matrizDicionario(matriz)
    elif (op == 0):

        break

