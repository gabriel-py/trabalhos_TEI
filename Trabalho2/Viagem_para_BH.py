#Ainda não está pronto
from collections import defaultdict
import heapq

class Viagem:

    def __init__(self):
        self.grafo = defaultdict(list)

    def add_aresta(self, A, B, R):
        self.grafo[A].append((B, R))

    def menor_caminho(self):
        pass


N, M = map(int, input().split())

viagem_onibus = Viagem()
viagem_aviao = Viagem()
print(N,M)
while True:
    try:
        A, B, T, R = map(int, input().split())
        if T == 1:
            viagem_aviao.add_aresta(A, B, R)
        else:
            viagem_onibus.add_aresta(A, B, R)
    except EOFError:
        break
