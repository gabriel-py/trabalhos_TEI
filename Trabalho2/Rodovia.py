# Gabriel Gonçalves de Souza Ribeiro - 20192003573
# João Francisco Carvalho Soares de Oliveira Queiroga - 20192020135
# Raquel Alexsandra do Couto - 201811130372

"""O problema se baseia em descobrir se o grafo direcionado é fortemente conexo (no caso, como o número de vertices e arestas são iguais, um grande ciclo), que saindo de um vertice é possivel chegar em todos os outros e retornar para ele mesmo. Para isso usamos o algoritmo DFS duas vezes: antes e após inverter o grafo. Assim, podemos nos assegurar de que partindo de qualquer vertice é possível chegar a qualquer outro"""

vert_arestas = int(input())

visitado = {} 
adjacencias = {}
for i in range(vert_arestas):
    adjacencias[i+1] = []
    
for i in range(vert_arestas):
    m, n = input().split(" ")
    m = int(m)
    n = int(n)
    adjacencias[m].append(n)
    visitado[i+1] = False

def verifica_visitado(visitado):
    for vert in visitado:
        if(visitado[vert]==False):
            return False
    return True


def dfs(vertice):
    fila = []
    fila.append(vertice)
    vizinhos = adjacencias[vertice]
    while(len(fila)!=0):
        vertice = fila[0]
        visitado[vertice] = True
        vizinhos = adjacencias[vertice]
        for vizin in vizinhos:
            if visitado[vizin] == False:
                fila.append(vizin)
        fila.pop(0)
        
dfs(1)

if(verifica_visitado(visitado)):
    
    ## Reseta o dic visitado
    for vert in visitado:
        visitado[vert] = False

    ##Inversão das adjacencias
    adjacencias_inversa = {}
    for i in range(vert_arestas):
        adjacencias_inversa[i+1] = []
        
    for vert in adjacencias:
        vertices_referenciados = adjacencias[vert]
        for ref in vertices_referenciados:
            adjacencias_inversa[ref].append(vert)
            
    adjacencias = adjacencias_inversa
    
    dfs(1)
    
    if(verifica_visitado(visitado)):
        print("S")
    else:
        print("N")
    
else:
    print("N")