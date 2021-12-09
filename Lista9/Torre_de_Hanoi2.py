#João Francisco Carvalho Soares de Oliveira Queiroga - 20192020135
#Gabriel Gonçalves de Souza Ribeiro - 20192003573
#Raquel Alexsandra do Couto - 201811130372
# A solucao implementada verifica, no momento de colocar a bola, se a soma da numero da bola a ser colocada com o 
#número da última bola da vareta forma um número quadrado. O numero de bolas colocadas é o numero da ultima bola - 1
def eh_quadrado(num):
    raiz = int(num ** (1/2))
    if (raiz ** 2) == num:
        return True
    else:
        return False
    
T = int(input())

for i in range(T):
    N = int(input())
    n_bola = 1
    arestas = [[] for j in range(N)]
    while True:
        colocado = False
        for aresta in arestas:
            if len(aresta) == 0 and not colocado:
                aresta.append(n_bola)
                colocado = True
                break
            elif eh_quadrado(aresta[-1] + n_bola) and not colocado:
                aresta.append(n_bola)
                colocado = True
                break
        if not colocado:
            break
        n_bola+=1
    print(n_bola - 1)
