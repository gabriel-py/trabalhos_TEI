#João Francisco Carvalho Soares de Oliveira Queiroga - 20192020135
#Gabriel Gonçalves de Souza Ribeiro - 20192003573
#Raquel Alexsandra do Couto - 201811130372
# A solução implementada testa as somas de numeros ao quadrado para verificar se o
#numero fornecido pode ser formado pela soma de dois quadrados
def forma_quadrados(num):
    if num < 0:
        return False
    num1 = int(num ** 0.5)
    num2 =  0
    while num1 >= num2:
        soma = (num1 ** 2) + (num2 ** 2)

        if soma == num:
            return True

        elif soma < num:
            num2+=1

        else:
            num1-=1

    return False

numeros = []
while True:
    try:
        numeros.append(int(input()))
    except EOFError:
        break

for numero in numeros:
    if forma_quadrados(numero):
        print("YES")
    else:
        print("NO")

