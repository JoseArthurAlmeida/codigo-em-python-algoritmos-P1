# Dada uma matriz N x N, escreva uma função que calcule a soma de todos os elementos da matriz.
from libMatriz import imprimeMatriz, criaMatriz

def somaElementos(matriz):
    return sum(sum(linha) for linha in matriz)

print("\033[1;44mOPERAÇÃO COM MATRIZES - SOMA DOS ELEMENTOS\033[m")

# Solicita ao usuário a quantidade de linhas e colunas para as matrizes
qtdLinhas = int(input("Digite a quantidade de linhas: "))
qtdColunas = int(input("Digite a quantidade de colunas: "))

matriz_A = criaMatriz(qtdLinhas, qtdColunas)

print("\n\033[1;42mMATRIZ 'A' CRIADA\033[m")
imprimeMatriz(matriz_A)

print("\n\033[1;42mSOMA DOS ELEMENTOS\033[m")
print(somaElementos(matriz_A))
