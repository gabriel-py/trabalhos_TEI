#
def eh_quadrado(num):
    raiz = int(num ** 1/2)
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
        n_bola+=1
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
    print(n_bola)
