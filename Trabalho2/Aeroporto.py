# Gabriel Gonçalves de Souza Ribeiro - 20192003573
# João Francisco Carvalho Soares de Oliveira Queiroga - 20192020135
# Raquel Alexsandra do Couto - 201811130372

# O programa se baseia em descobrir qual ou quais vertices possuem o maior grau (de onde mais sai e chega arestas)


teste = 1
while True:
    a, v = [int(i) for i in input().split()]
    if a == v == 0:
        break

    aero = [0] * a
    while v:
        v -= 1
        x, y = [int(i) for i in input().split()]
        aero[x-1] += 1
        aero[y-1] += 1

    m = max(aero)
    maior = [str(i + 1) for i in range(len(aero)) if aero[i] == m]
    print('Teste %d' % teste)
    teste += 1
    print(' '.join(maior), '')
    print()