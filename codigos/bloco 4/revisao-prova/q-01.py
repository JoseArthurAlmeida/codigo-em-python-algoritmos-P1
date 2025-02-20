# Escreva uma função em Python que crie uma matriz N x N preenchida com zeros.
from libMatriz import imprimeMatriz

def criaMatriz(linhas, colunas):
    matriz = []
    for indiceLinha in range(linhas):
        linha = []
        for indiceColuna in range(colunas):
            linha.append(0)
        matriz.append(linha)
    return matriz

print("\033[1;44mOPERAÇÃO COM MATRIZES - MATRIZ 0\033[m")

# Solicita ao usuário a quantidade de linhas e colunas para as matrizes
qtdLinhas = int(input("Digite a quantidade de linhas: "))
qtdColunas = int(input("Digite a quantidade de colunas: "))

matriz_A = criaMatriz(qtdLinhas, qtdColunas)

print("\n\033[1;42mMATRIZ 'A' CRIADA\033[m")
imprimeMatriz(matriz_A)