# O seguinte algoritmo recebe uma sequência de números inteiros do usuário, armazenando em uma lista,
# e realiza algumas operações de: encontrar o maior, o menor, a soma e ordená-los.
listaNumeros = []

numero = int(input("Digite um número: "))

while numero != 0:
    listaNumeros.append(numero)
    numero = int(input("Digite um número: "))

listaNumeros.sort()

print(f"Maior: {listaNumeros[-1]}, Menor: {listaNumeros[0]}")
print(f"Soma = {sum(listaNumeros)}")
print(f"Maior = {max(listaNumeros)}, Menor: {min(listaNumeros)}")