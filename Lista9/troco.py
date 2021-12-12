#João Francisco Carvalho Soares de Oliveira Queiroga - 20192020135
#Gabriel Gonçalves de Souza Ribeiro - 20192003573
#Raquel Alexsandra do Couto - 201811130372
#A solução empregada analisa o valor das moedas para ver se é possível,
# ao somar o valor de combinações dessas moedas, obter o valor exato da compra.
V, M = map(int, input().split())

somas_possiveis = [False for i in range(V + 1)]
somas_possiveis[0] = True

moedas = input().split()
moedas = [int(moedas[i]) for i in range(M)]

for moeda in moedas:
    for i in range(V, moeda - 1, -1):
        if somas_possiveis[i - moeda]:
            somas_possiveis[i] = True

if somas_possiveis[V]:
    print("S")
else:
    print("N")
