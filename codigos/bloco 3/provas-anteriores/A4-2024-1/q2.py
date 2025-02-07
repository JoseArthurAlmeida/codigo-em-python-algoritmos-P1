# Crie uma função recursiva em Python que calcula a soma dos dígitos de um número inteiro positivo.
# A soma dos dígitos é obtida somando todos os dígitos que compõem o número.

def somaDigitos(numero):
    if numero < 10:
        return numero
    
    return somaDigitos(numero // 10) + somaDigitos(numero % 10)

for i in range(6):
    entrada = int(input())
    print(f"{entrada} -> {somaDigitos(entrada)}")