# Escreva uma função que conte quantos números pares existem em uma matriz N x N.
from libMatriz import imprimeMatriz, criaMatriz

def contaPares(matriz):
    contador = 0
    for linha in matriz:
        for elemento in linha:
            if (elemento % 2) == 0: contador += 1
    
    return contador

print("\033[1;44mOPERAÇÃO COM MATRIZES - MULTIPLICAÇÃO POR ESCALAR\033[m")

qtdLinhas = int(input("Digite a quantidade de linhas da Matriz A: "))
qtdColunas = int(input("Digite a quantidade de colunas da Matriz A: "))

print()
print("\033[1;41mCRIANDO A MATRIZ:\033[m ")
# Cria a primeira matriz com os valores fornecidos pelo usuário

matriz_A = criaMatriz(qtdLinhas, qtdColunas)

print("\n\033[1;42mMATRIZ CRIADA: A\033[m")
imprimeMatriz(matriz_A)

print("\n\033[1;42mCONTANDO PARES\033[m")
print(contaPares(matriz_A))
