#João Francisco Carvalho Soares de Oliveira Queiroga - 20192020135
#Gabriel Gonçalves de Souza Ribeiro - 20192003573
#Raquel Alexsandra do Couto - 201811130372
#A solução impĺemrntada faz uma busca de profundidade na matriz de adjacencia e verificar se todos os vértices foram visitados.
#Não foi preciso criar uma estrutura armazenando os dados em sí já que era somente necessário checar se os vértices estavam todos ligados entre sí.
def dfs(vertice, visitados = []):
    visitados.append(vertice)
    vertice-=1
    for i in range(N):
        if ligacoes[vertice][i] == 1 and i + 1 not in visitados:
            dfs(i + 1, visitados)
    return visitados


def faz_ligacao(vertice1, vertice2):
    ligacoes[vertice1-1] [vertice2-1] = 1
    ligacoes[vertice2-1][vertice1-1] = 1

N, L = map(int, input().split())
ligacoes = [[0 for j in range(N)] for i in range(N)]
n_pre, n_pos = 1, 1
for i in range(L):
    x, y = map(int, input().split())
    faz_ligacao(x, y)

visitados = dfs(1)
if len(visitados) == N:
    print("COMPLETO")
else:
   print("INCOMPLETO")
