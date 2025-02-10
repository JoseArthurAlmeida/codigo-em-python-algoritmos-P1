# 14. Escreva uma função recursiva para calcular a soma dos cubos dos primeiros n números naturais.
numero = int(input("Digite um número: "))

def somaRecursivaCubos(n):
    if n == 0:
        return n
    return n ** 3 + somaRecursivaCubos(n - 1)

print(somaRecursivaCubos(numero))