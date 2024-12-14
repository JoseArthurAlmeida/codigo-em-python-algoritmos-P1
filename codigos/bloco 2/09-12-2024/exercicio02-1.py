# Algoritmo que calcula a média, a mediana, e a moda de uma lista de números
listaNumeros = []
quantidades = []

for i in range(10):
    numero = int(input("Digite um número: "))
    listaNumeros.append(numero)

def ehPar(num):
    return (num % 2) == 0

def calcularMediana(lista):
    tamanhoLista = len(lista)
    listaOrdenada = sorted(lista)

    if ehPar(tamanhoLista):
        
        valor1 = listaOrdenada[int(tamanhoLista / 2) - 1]
        valor2 = listaOrdenada[int(tamanhoLista / 2)]
        # print(f"{int(tamanhoLista / 2) - 1}, {int(tamanhoLista / 2)}")
        # print(f'{valor1},{valor2}')

        return (valor1 + valor2) / 2
    else:
        return listaOrdenada[int(tamanhoLista / 2)] 

for k in listaNumeros:
    quantidades.append(listaNumeros.count(k))

maiorQuantidades = max(quantidades)
posicaoDesejada = quantidades.index(maiorQuantidades)

media = sum(listaNumeros) / len(listaNumeros)
mediana = calcularMediana(listaNumeros)
moda = listaNumeros[posicaoDesejada]

print(f"lista normal: {listaNumeros}")
# print(f"qtd: {quantidades}")
print(f"Lista ordenada: {sorted(listaNumeros)}")
print(f"Média = {media}")
print(f"Mediana = {mediana}")
print(f"Moda = {moda}")