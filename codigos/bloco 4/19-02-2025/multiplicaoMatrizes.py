from libMatriz import criaMatriz, imprimeMatriz

def multiplicacao(a, b):
    resultadoMatriz = []
    
    for indiceLinhaMatriz_A in range(len(a)): # indice da linha da matriz A
        linhaTemp = []
        for indiceColunaMatriz_B in range(len(b[0])): # indice da coluna da matriz B 
            resultadoTemp = 0

            for indiceLinhaMatriz_B in range(len(b)): # indice da linha da matriz B
                resultadoTemp += a[indiceLinhaMatriz_A][indiceLinhaMatriz_B] * b[indiceLinhaMatriz_B][indiceColunaMatriz_B]

            linhaTemp.append(resultadoTemp)
        resultadoMatriz.append(linhaTemp)

    return resultadoMatriz

print("\033[1;44mOPERAÇÃO COM MATRIZES - MULTIPLICAÇÃO DE MATRIZES\033[m")

qtdLinhasA = int(input("Digite a quantidade de linhas da Matriz A: "))
qtdColunasA = int(input("Digite a quantidade de colunas da Matriz A: "))

print("\n\033[1;41mCRIANDO A MATRIZ 'A':\033[m ")
matriz_A = criaMatriz(qtdLinhasA, qtdColunasA)

# Imprime a matriz A
print("\n\033[1;42mMATRIZ CRIADA 'A':\033[m ")
imprimeMatriz(matriz_A)

print()
qtdLinhasB = int(input("Digite a quantidade de linhas da Matriz B: "))
qtdColunasB = int(input("Digite a quantidade de colunas da Matriz B: "))

print("\n\033[1;41mCRIANDO A MATRIZ 'B':\033[m ")
matriz_B = criaMatriz(qtdLinhasB, qtdColunasB)

# Imprime a matriz B
print("\n\033[1;42mMATRIZ CRIADA 'B':\033[m ")
imprimeMatriz(matriz_B)

# Verifica se é possível multiplicar as matrizes
if qtdColunasA != qtdLinhasB:
    print("\033[1;31mNão é possível multiplicar as matrizes. O número de colunas da matriz A deve ser igual ao número de linhas da matriz B.\033[m")
else:
    print("\n\033[1;43mMATRIZ A * B:\033[m ")
    imprimeMatriz(multiplicacao(matriz_A, matriz_B))