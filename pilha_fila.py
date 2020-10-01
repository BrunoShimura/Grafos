# funcões
def Push (P, topo, v):# insere o  lemento na pilha
    P.insert(topo,v)

def Pop (P):# remove o  lemento na pilha
    P.pop()

# array de 20 posições
P = []*20
topo = 0
#while True:
    #v = input("Digite o vertice a inserir ou Fim para encerrar: ")
    #if v == "Fim":
    #    break
    #Push (P,topo,v)
    #topo += 1

topo -= 1
#Pop(P)
#print(P)

#===========================================================
def Inserir(F,Fim,v):
    F.insert(Fim,v)
def Remover(F,Inicio):
    F.pop(Inicio)
F = []*20
Inicio = 0
Fim = 0

while True:
    v = input("Digite o vertice a inserir ou Fim para encerrar: ")
    if v == "Fim":
        break
    Inserir (F,Fim,v)
    Fim += 1

print(F)
Remover(F,Inicio)
print(F)
