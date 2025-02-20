# Crie uma função que multiplique uma matriz N x N por um número X qualquer.
from libMatriz import criaMatriz, imprimeMatriz

def produtoPorEscalar(matriz, escalar):
   return [[elemento * escalar for elemento in linha] for linha in matriz]

# Solicita ao usuário a quantidade de linhas e colunas para as matrizes
print("\033[1;44mOPERAÇÃO COM MATRIZES - MULTIPLICAÇÃO POR ESCALAR\033[m")

qtdLinhas = int(input("Digite a quantidade de linhas da Matriz A: "))
qtdColunas = int(input("Digite a quantidade de colunas da Matriz A: "))

print()
print("\033[1;41mCRIANDO A MATRIZ:\033[m ")
# Cria a primeira matriz com os valores fornecidos pelo usuário

matriz_A = criaMatriz(qtdLinhas, qtdColunas)

print("\n\033[1;42mMATRIZ CRIADA: A\033[m")
imprimeMatriz(matriz_A)

print()
escalar = int(input("Digite a escalar: "))
print("\033[1;43mMATRIZ MULTIPLICADA PELO ESCALAR\033[m")
imprimeMatriz(produtoPorEscalar(matriz_A, escalar))