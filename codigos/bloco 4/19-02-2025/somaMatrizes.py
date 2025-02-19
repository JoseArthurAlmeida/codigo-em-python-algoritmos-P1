from libMatriz import criaMatriz, imprimeMatriz

def somaMatrizes(matriz_1, matriz_2, linhas, colunas):
    # Soma duas matrizes de mesmo tamanho e retorna a matriz resultante
    matriz = []
    for i in range(linhas):
        linha = []
        for j in range(colunas):
            linha.append(matriz_1[i][j] + matriz_2[i][j])
        matriz.append(linha)
    return matriz

print("\033[1;44mOPERAÇÃO COM MATRIZES - SOMA DE MATRIZES\033[m")

# Solicita ao usuário a quantidade de linhas e colunas para as matrizes
qtdLinhas = int(input("Digite a quantidade de linhas: "))
qtdColunas = int(input("Digite a quantidade de colunas: "))

print("\n\033[1;41mCRIANDO A MATRIZ 'A':\033[m")
# Cria a primeira matriz com os valores fornecidos pelo usuário
matriz_A = criaMatriz(qtdLinhas, qtdColunas)

print("\n\033[1;42mMATRIZ 'A' CRIADA\033[m")
imprimeMatriz(matriz_A)

print("\n\033[1;41mCRIANDO A MATRIZ 'B':\033[m")
# Cria a segunda matriz com os valores fornecidos pelo usuário
matriz_B = criaMatriz(qtdLinhas, qtdColunas)

print("\n\033[1;42mMATRIZ 'B' CRIADA\033[m")
imprimeMatriz(matriz_B)

print("\n\033[1;43mSOMA DAS MATRIZES:\033[m ")
soma = somaMatrizes(matriz_A, matriz_B, qtdLinhas, qtdColunas)
imprimeMatriz(soma)