# Crie uma função que receba uma matriz N x N e substitua todos os elementos da diagonal principal por 1.
from libMatriz import imprimeMatriz, criaMatriz

def substitueDiagonalPrincipal(matriz):
    for i in range(len(matriz)):
       matriz[i][i] = 1

def simetrica(matriz_1, matriz_2):
    return matriz_1 == matriz_2

# Solicita ao usuário a quantidade de linhas e colunas para as matrizes
print("\033[1;44mOPERAÇÃO COM MATRIZES - substitua todos os elementos da diagonal principal por 1.\033[m")

qtdLinhas = int(input("Digite a quantidade de linhas da Matriz A: "))
qtdColunas = int(input("Digite a quantidade de colunas da Matriz A: "))

print()
print("\033[1;41mCRIANDO A MATRIZ:\033[m ")
matriz_A = criaMatriz(qtdLinhas, qtdColunas)

print("\n\033[1;42mMATRIZ 'A' CRIADA\033[m")
imprimeMatriz(matriz_A)

print("\n\033[1;42msubstitua todos os elementos da diagonal principal por 1.\033[m")
substitueDiagonalPrincipal(matriz_A)
imprimeMatriz(matriz_A)