# 7. Crie uma função recursiva para converter um número decimal em binário.
decimal = int(input("Digite um número decimal: "))

def decimalParaBinario(numero):
    if numero == 0:
        return ""
    
    return decimalParaBinario(numero // 2) + str(numero % 2)

print(decimalParaBinario(decimal))