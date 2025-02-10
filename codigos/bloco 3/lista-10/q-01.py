# 1. Crie uma função recursiva que retorne a soma dos primeiros `n` números naturais.
numero = int(input("Digite um número: "))

# n = 5 => 5 + 4 + 3 + 2 + 1 => 15

def somaRecursiva(n):
    if n == 0:
        return n
    return n + somaRecursiva(n - 1)

print(somaRecursiva(numero))