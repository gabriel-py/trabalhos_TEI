# Gabriel Gonçalves de Souza Ribeiro - 20192003573
# João Francisco Carvalho Soares de Oliveira Queiroga - 20192020135
# Raquel Alexsandra do Couto - 201811130372

# O programa se baseia em descobrir qual ou quais vertices possuem o maior grau (de onde mais sai e chega arestas)

teste = 1
while True:
    qtd_vertices, qtd_arestas = map(int, input().split())
    
    if qtd_vertices == qtd_arestas ==0:
        break



    arestas = []
    for i in range(qtd_arestas):
        a, b = map(int, input().split())
        arestas.append([a,b])
        
    grau_vertice = {}
    for j in range(qtd_vertices):
        num_vertice = j+1
        cont=0
        for lista in arestas:
            if num_vertice in lista:
                cont+=1
        grau_vertice[num_vertice] = cont
    
    maior_grau = [ [-1, -1] ]
    for vertice in grau_vertice:
        if grau_vertice[vertice] > maior_grau[0][1]:
            maior_grau = []
            maior_grau.append([vertice, grau_vertice[vertice]])
        elif grau_vertice[vertice] == maior_grau[0][1]:
            maior_grau.append([vertice, grau_vertice[vertice]])
            
    print("Teste", teste)
    
    if len(maior_grau) == 1:
        print(maior_grau[0][0], '')
    else:
        saida = [str(maior_grau[i][0]) for i in range(len(maior_grau))] 
        print(" ".join(saida),'')
    print()

    teste+=1
