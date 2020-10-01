def grau(a):
    cont = 0
    for i in a:
        cont+=1
    return cont

def insereAresta(g, a, b):
    if a not in g:
        g[a] = []
    if b not in g:
        g[b] = []
    g[a].append(b)
    g[b].append(a)

def imprimeGrafo(g):
    for v,a in g.items():
        print("="*50)
        print("Vertice: ", v)
        print("Adjacentes: ", a)
        print("Grau: ", grau(a))

#dado um grafo e um vértice, retorne com um grau (numero inteiro das arestas incidentes)

grafo = { }
while True:
    x = input("Entre com o vertice ou FIM para encerrar: ")
    if x == "FIM":
        break
    y = input("Entre com o vertice adjacente: ")

    insereAresta(grafo, x, y)

imprimeGrafo(grafo)