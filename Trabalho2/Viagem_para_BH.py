#Ainda não está pronto
def dfs(vertice, caminho = []):
    pass

N, M = map(str, input().split())

grafo_onibus = []
grafo_aviao = []

while True:
    try:
        A, B, T, R = map(int, input().split())
        if T == 1:
            grafo_aviao.append([A, [B, R]])
        else:
            grafo_onibus.append([A, B, R])
    except EOFError:
        break
