#
def eh_quadrado(num):
    raiz = int(num ** 1/2)
    if raiz ** 2 == num:
        return True
    else:
        return False

T = int(input())

for i in range(T):
    N = int(input())
    n_bola = 1
