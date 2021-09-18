# Gabriel Gonçalves de Souza Ribeiro - 20192003573
# João Francisco Carvalho Soares de Oliveira Queiroga - 20192020135
# Raquel Alexsandra do Couto - 201811130372

"""O problema se baseia em descobrir se o grafo é um grande ciclo, que saindo de um dado vértice é possivel voltar para ele mesmo, depois de percorrer todos os outros vertices do grafo"""


vert_arestas = int(input())

vertices_visita = {} 
adjacencia = {}
for i in range(vert_arestas):
    m, n = input().split(" ")
    m = int(m)
    n = int(n)
    adjacencia[m] = n
    vertices_visita[i+1] = False

exit = 0
if(len(adjacencia)<vert_arestas):
    print("N")
    exit = 1

def verifica_todos_visitados(vertices_visita):
    for vert in vertices_visita:
        if(vertices_visita[vert]):
            continue
        else:
            return False
    return True

ini = 1
inicial = 1
if(exit==0):
    while(True):
        vertices_visita[inicial] = True
        inicial = adjacencia[inicial]
        verifica = verifica_todos_visitados(vertices_visita)
        if(inicial == ini and verifica):
            print("S")
            break;
        if(inicial != ini and verifica):
            print("N")
            break;
        if(inicial == ini and verifica==False):
            print("N")
            break;