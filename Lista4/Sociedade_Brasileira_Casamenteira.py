#João Francisco Carvalho Soares de Oliveira Queiroga - 20192020135
#Gabriel Gonçalves de Souza Ribeiro - 20192003573
#Raquel Alexsandra do Couto - 201811130372
#A solução implementada transforma os pares de pessoas apaixonadas em um grafo ordenado em que cada pessoa é uma aresta
#e está ligada ao vértice em que esta pessoa está apaixonada.
#é feita então uma DFS para ver se é completado um ciclo no grafo ordenado da pesssoa até ela mesma
#cada ciclo completo é um casal formado.

def dfs(vertice, caminho = []):
    caminho.append(vertice)
    for vizinho in grafo[vertice]:
        if caminho[len(caminho) - 1] == caminho[0]:
            return caminho
        if vizinho not in caminho or vizinho == caminho[0]:
            dfs(vizinho, caminho)
        return caminho

def tem_ciclo(vertice):
    busca = dfs(vertice)
    if busca[0] == busca[len(busca)-1]:
        return True
    else:
        return False

def cria_adjacencia(par):
    for i in range(n_pessoas):
        if pessoas[i] == par[0]:
            for j in range(n_pessoas):
                if pessoas[j] == par[1]:
                    grafo[i].append(j)
                    return
paixoes = []
while True:
    try:
        paixoes.append(input().split())
    except EOFError:
        break

pessoas = []

for par in paixoes:
    for pessoa in par:
        if pessoa not in pessoas:
            pessoas.append(pessoa)

n_pessoas = len(pessoas)

grafo = [[] for j in range(n_pessoas)]
verificado = [0 for i in range(n_pessoas)]
for par in paixoes:
    cria_adjacencia(par)

n_casais = 0

print(grafo)

for i in range(n_pessoas):
    if verificado[i] == 0 and tem_ciclo(i):
        n_casais += 1
print(n_casais)
