# Gabriel Gonçalves de Souza Ribeiro - 20192003573
# João Francisco Carvalho Soares de Oliveira Queiroga - 20192020135
# Raquel Alexsandra do Couto - 201811130372
#O código usa o algoritimo de Djikstra para verificar os menores caminhos e usa o maior entre esses caminhos.

from heapq import heappush, heappop

def menor_caminho(grafo, origem):
        anterior = [-1] * (N)
        distancia = [float('inf')] * (N)
        anterior[origem] = origem
        distancia[origem] = 0
        fila_prioridade = []
        heappush(fila_prioridade, (0, origem))

        while fila_prioridade:
            dist, u = heappop(fila_prioridade)

            if dist > distancia[u]:
                continue
            
            for v, peso in grafo[u]:
                if distancia[u] + peso < distancia[v]:
                    distancia[v] = distancia[u] + peso
                    anterior[v] = u
                    heappush(fila_prioridade, (distancia[v], v))

        return max(distancia)


N, M = map(int, input().split())

cidades = [[] for i in range(N)]

for i in range(M):
    U, V, W = map(int, input().split())
    cidades[U].append((V, W))
    cidades[V].append((U, W))

tamanhos = [menor_caminho(cidades, i) for i in range(N)]

print(min(tamanhos))
