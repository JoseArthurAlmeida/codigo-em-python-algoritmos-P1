# 5. Crie uma função recursiva para encontrar o número de dígitos de um número inteiro.
entrada = input("Digite um número: ")

def numeroDigitos(numero):
    if len(numero) == 1:
        return 1
    
    if numero.startswith("-"):
        numero = numero[1:]
    
    return 1 + numeroDigitos(numero[1:])

print(numeroDigitos(entrada))