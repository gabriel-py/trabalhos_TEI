# Gabriel Gonçalves de Souza Ribeiro - 20192003573
# João Francisco Carvalho Soares de Oliveira Queiroga - 20192020135
# Raquel Alexsandra do Couto - 201811130372

"""O problema se baseia em descobrir quantos grafos conexos (pontos isolados da cidade) existem dado o grafo desconexo dado. Para isso basta utilizar o algoritmo de busca em profundidade (DSF), que percorre todos os vértices do grafo. Os vértices que não forem vistitados são aqueles desconexos ao restante do grafo."""


casos_teste = int(input())

for i in range(casos_teste):
    
    x = input()
    if(' ' not in str(x)):
        qtd_arestas = int(input())
        qtd_vertices = int(x)
    else:
        qtd_vertices, qtd_arestas = x.split()
        qtd_vertices = int(qtd_vertices)
        qtd_arestas = int(qtd_arestas)
    
    list_adj = {}
    visitado = {}
    for j in range(qtd_vertices):
        list_adj[j+1] = []
        visitado[j+1] = False
    
    for k in range(qtd_arestas):
        n, m = input().split(' ')
        n = int(n)
        m = int(m)
        list_adj[n].append(m)
        list_adj[m].append(n)
    
    """list_adj = {1: [2,3, 4], 2: [1, 3], 3: [1, 2, 4], 4: [1, 3], 5: [], 6: []}

    visitado = {1: False, 2: False, 3: False, 4: False, 5: False, 6: False}"""
    
    
    def dfs(vertice):
        visitado[vertice] = True
        vizinhos = list_adj[vertice]
        for vizin in vizinhos:
            if visitado[vizin] == False:
                dfs(vizin)
                
    
    conexo=0
    for vert in list_adj:
        if(visitado[vert]==False):
            dfs(vert)
            conexo=conexo+1
    
    resp = conexo-1
    if(resp==0):
        print("Caso #"+str(i+1)+": a promessa foi cumprida")
    else:
        print("Caso #"+str(i+1)+": ainda falta(m) "+str(resp)+" estrada(s)")