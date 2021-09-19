# Gabriel Gonçalves de Souza Ribeiro - 20192003573
# João Francisco Carvalho Soares de Oliveira Queiroga - 20192020135
# Raquel Alexsandra do Couto - 201811130372

"""O problema se baseia em descobrir a arvore geradora minima do grafo dado. Para isso, usamos o algoritmo de Kruskal."""


import heapq

teste = 0
while(True):
    teste = teste+1
    
    try:
        x = input()
        if(' ' not in str(x)):
            vert = int(input())
            arestas = int(x)
        else:
            vert, arestas = x.split()
            vert = int(vert)
            arestas = int(arestas)
    except EOFError:
        break;
    
    if(vert==0 and arestas==0):
        break;
    
    H = []
    for i in range(arestas):
        m, n, p = input().split()
        m = int(m)
        n = int(n)
        p = int(p)
        heapq.heappush(H, (p, m, n))
    
    C = {}
    for i in range(vert):
        C[i+1] = i+1
    
    A = []
    cont = 0
    while cont < vert-1:
        p, m, n = heapq.heappop(H)
        if(C[m] != C[n]):
            if m>n:
                A.append([n, m])
            else:
                A.append([m, n])
            for vert in C:
                if(C[vert]==C[m]):
                    C[vert] = C[n]
            cont = cont+1
            
    print("Teste "+str(teste))
    for aresta in A:
        print(str(aresta[0])+" "+str(aresta[1]))
    print()