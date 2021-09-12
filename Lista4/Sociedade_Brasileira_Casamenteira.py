#João Francisco Carvalho Soares de Oliveira Queiroga - 20192020135
#Gabriel Gonçalves de Souza Ribeiro - 20192003573
#Raquel Alexsandra do Couto - 201811130372
#A solução implementada usa dicionarios para armazenar o grafo em que cada pessoa é um nó e é ligado a outra..
#É feita então uma DFS para ver se é completado um ciclo no grafo ordenado da pesssoa até ela mesma
#cada ciclo completo é um casal formado.

def dfs(vertice_inicio):
    caminho = [vertice_inicio]
    falta_visitar = [vertice_inicio]
    while falta_visitar:
        vertice = falta_visitar.pop()
        if len(caminho) > 1 and vertice == caminho[0]:
            return caminho
        if grafo[vertice] not in caminho or grafo[vertice] == caminho[0]:
            caminho.append(grafo[vertice])
            falta_visitar.append(grafo[vertice])
    return caminho

def tem_ciclo(vertice):
    busca = dfs(vertice)
    if busca[0] == busca[len(busca)-1]:
        for vertice in busca:
            verificado[vertice] = True
        return True
    else:
        return False

grafo = dict()
verificado = dict()
while True:
    try:
        nome1, nome2 = map(str, input().split())
        grafo[nome1] = nome2
        verificado[nome1] = False
    except EOFError:
        break

n_casais = 0

for vertice in grafo:
    if verificado[vertice] == False and tem_ciclo(vertice):
        n_casais += 1
print(n_casais)
