#João Francisco Carvalho Soares de Oliveira Queiroga - 20292020135
#Gabriel Gonçalves de Souza Ribeiro - 20192003573
#Raquel Alexsandra do Couto - 201811130372
#A solução implementada consiste em armazenar o mapa em uma matriz e verificar se
#havia alguma borda ou espaço com água adjacente a cada espaço de terra.  
def verificaLitoral(x, y) -> bool:
    if mapa[x][y] == '.':
        return False
    elif x == 0 or y == 0 or x == M - 1 or y == N - 1:
        return True
    else:
        if x < M - 2:
            if mapa[x+1][y] == '.':
                return True
    
        if x > 0:
            if mapa[x-1][y] == '.':
                return True
    
        if y <= N - 1:
            if mapa[x][y+1] == '.':
                return True
    
        if x > 0:
            if mapa[x][y-1] == '.':
                return True
        return False

M, N = map(int, input().split())
mapa = [list(input()) for j in range(M)]
litorais = 0
for x in range(M):
    for y in range(N):
        if verificaLitoral(x,y):
            litorais+=1

print(litorais)/
