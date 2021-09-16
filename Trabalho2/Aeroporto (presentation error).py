# Gabriel Gonçalves de Souza Ribeiro - 20192003573
# João Francisco Carvalho Soares de Oliveira Queiroga - 20192020135
# Raquel Alexsandra do Couto - 201811130372

# O programa se baseia em descobrir qual ou quais vertices possuem o maior grau (de onde mais sai e chega arestas)

teste = 1
while(True):
    qtd_vertices, qtd_arestas = input().split()
    qtd_vertices = int(qtd_vertices)
    qtd_arestas = int(qtd_arestas)
    
    if(qtd_vertices==0 and qtd_arestas==0):
        break;
    
    arestas = []
    for i in range(qtd_arestas):
        a, b = input().split()
        a = int(a)
        b = int(b)
        arestas.append([a,b])
        
    grau_vertice = {}
    for j in range(qtd_vertices):
        num_vertice = j+1
        cont=0
        for lista in arestas:
            if(num_vertice in lista):
                cont = cont+1
        grau_vertice[num_vertice] = cont
    
    maior_grau = [ [-1, -1] ]
    for vertice in grau_vertice:
        if(grau_vertice[vertice]>maior_grau[0][1]):
            maior_grau = []
            maior_grau.append([vertice, grau_vertice[vertice]])
        elif(grau_vertice[vertice]==maior_grau[0][1]):
            maior_grau.append([vertice, grau_vertice[vertice]])
            
    print("Teste "+str(teste))
    
    if(len(maior_grau)==1):
        print(str(maior_grau[0][0]))
        print()
    else:
        tamanho = len(maior_grau)
        saida = ""
        for k in range(tamanho):
            saida = saida + str(maior_grau[k][0]) + " "
        saida = saida[:-1]
        print(saida)
        print()
    
    teste=teste+1;