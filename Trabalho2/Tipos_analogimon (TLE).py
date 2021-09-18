# Gabriel Gonçalves de Souza Ribeiro - 20192003573
# João Francisco Carvalho Soares de Oliveira Queiroga - 20192020135
# Raquel Alexsandra do Couto - 201811130372

"""O problema se baseia em descobrir a quantos vértices (espécies) é possível chegar partindo de um vérice inicial (a espécie informada). Para isso, usamos o algoritmos DFS passando como vérice inicial a 'espécie informada' e ao final contamos quantos vértices foram percorridos"""

adjacencias = {}
visitado = {}

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

while True:
    try:
        vertices, arestas = input().split()
        vertices = int(vertices)
        arestas = int(arestas)
        
        for i in range(vertices):
            adjacencias[i+1] = []
            visitado[i+1] = False
            
        for i in range(arestas):
            m, n = input().split()
            m = int(m)
            n = int(n)
            adjacencias[m].append(n)
            adjacencias[n].append(m)
            
        tipo_anal = int(input())
        
        dfs(tipo_anal)
        
        cont = 0
        for vert in visitado:
            if(visitado[vert]==True):
                cont=cont+1
                
        print(cont)
        
        adjacencias = {}
        visitado = {}
        cont = 0
        
    except EOFError:
        break