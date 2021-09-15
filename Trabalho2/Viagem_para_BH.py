#Ainda não está pronto
def menor_preco(array):
    menor = array[0][1]
    for i in range(len(array)):
        if array[i][1] < menor:
            menor = array[i][1]
    return menor


def dfs(vertice_fonte):
    nao_resolvido = [vertice_fonte]
    while nao_resolvido:
        vertice = nao_resolvido.pop(menor_preco(nao_resolvido))

N, M = map(int, input().split())

grafo_onibus = [[] for i in range(N)]
grafo_aviao = [[] for i in range(N)]

while True:
    try:
        A, B, T, R = map(int, input().split())
        if T == 1:
            grafo_aviao[A - 1].append([B, R])
            pass
        else:
            grafo_onibus[A - 1].append([B, R])
    except EOFError:
        break
print(grafo_onibus)
