# Gabriel Gonçalves de Souza Ribeiro - 20192003573
# João Francisco Carvalho Soares de Oliveira Queiroga - 20192020135
# Raquel Alexsandra do Couto - 201811130372

"""O problema se baseia em descobrir quais vertices não estão conexos ao restante do grafo. Tais vertices (bairros) não podem ser alcançados a partir dos outros por justamente não haver caminhos (arestas). Para descobrir os vértices desconexos usamos o algoritmo de busca em profundidade DFS."""

num_bairros, num_conexoes, num_perguntas = input().split(" ")
num_bairros = int(num_bairros)
num_conexoes = int(num_conexoes)
num_perguntas = int(num_perguntas)

adjacencias = {}
visitado = {}
for i in range(num_bairros):
    adjacencias[i+1] = []
    visitado[i+1] = False
    
for i in range(num_conexoes):
    m, n = input().split(" ")
    m = int(m)
    n = int(n)
    adjacencias[m].append(n)
    adjacencias[n].append(m)

perguntas = []
for i in range(num_perguntas):
    m, n = input().split(" ")
    m = int(m)
    n = int(n)
    perguntas.append([m, n])

num_grafo = 1
def dfs(de):
    visitado[de] = num_grafo
    vizinhos = adjacencias[de]
    for vizin in vizinhos:
        if visitado[vizin] == False:
            dfs(vizin)
            
dfs(1)
for vert in visitado:
    if(visitado[vert]==False):
        num_grafo = num_grafo + 1
        dfs(vert)

for pergunta in perguntas:
    de = pergunta[0]
    para = pergunta[1]
    if(visitado[de]==visitado[para]):
        print("Lets que lets")
    else:
        print("Deu ruim")