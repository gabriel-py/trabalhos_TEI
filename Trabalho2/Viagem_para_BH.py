#Ainda não está pronto
def dfs(vertice, caminho = []):
    pass

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
print(grafo_aviao)
