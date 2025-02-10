# 13. Implemente uma função recursiva para calcular a soma dos quadrados dos primeiros n números naturais.
numero = int(input("Digite um número: "))

# n = 5 => 5 ^2 + 4 + 3 + 2 + 1 => 15

def somaRecursivaQuadrados(n):
    if n == 0:
        return n
    return n ** 2 + somaRecursivaQuadrados(n - 1)

print(somaRecursivaQuadrados(numero))