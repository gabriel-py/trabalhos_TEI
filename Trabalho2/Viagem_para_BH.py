# Gabriel Gonçalves de Souza Ribeiro - 20192003573
# João Francisco Carvalho Soares de Oliveira Queiroga - 20192020135
# Raquel Alexsandra do Couto - 201811130372
#O Código usa o algoritimo de Dijkstra para achar o menor caminho e então compara os caminhos do onibus e do avião

from heapq import heappush, heappop

class Viagem:

    def __init__(self, N):
        self.grafo = [[] for i in range(N + 1)]
        self.num_v = N

    def add_aresta(self, A, B, R):
        self.grafo[A].append((B, R))

    def menor_caminho(self, origem):
        anterior = [-1] * (self.num_v + 1)
        distancia = [float('inf')] * (self.num_v + 1)
        anterior[origem] = origem
        distancia[origem] = 0
        fila_prioridade = []
        heappush(fila_prioridade, (0, origem))

        while fila_prioridade:
            dist, u = heappop(fila_prioridade)

            if dist > distancia[u]:
                continue
            
            for v, peso in self.grafo[u]:
                if distancia[u] + peso < distancia[v]:
                    distancia[v] = distancia[u] + peso
                    anterior[v] = u
                    heappush(fila_prioridade, (distancia[v], v))

        return distancia



while True:
    try:
        N, M = map(int, input().split())
        viagem_onibus = Viagem(N)
        viagem_aviao = Viagem(N)
        for i in range(M):
            A, B, T, R = map(int, input().split())
            if T == 1:
                viagem_aviao.add_aresta(A, B, R)
            else:
                viagem_onibus.add_aresta(A, B, R)

        preco_aviao = viagem_aviao.menor_caminho(1)
        preco_onibus = viagem_onibus.menor_caminho(1)

        preco_aviao = preco_aviao[len(preco_aviao) - 1]
        preco_onibus = preco_onibus[len(preco_onibus) - 1]

        if preco_aviao < preco_onibus:
            print(preco_aviao)
        else:
            print(preco_onibus)
    except EOFError:
        break
