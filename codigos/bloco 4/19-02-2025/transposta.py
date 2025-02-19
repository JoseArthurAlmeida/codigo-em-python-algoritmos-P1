from libMatriz import criaMatriz, imprimeMatriz

def transposta(matriz):
    # Cria uma matriz transposta da matriz
    matrizTransposta = []

    # Iterar pelos indices da coluna 
    for coluna in range(len(matriz[0])):
        linhaMatriz = []
        # Iterar pelos indices da linha
        for linha in range(len(matriz)):
            linhaMatriz.append(matriz[linha][coluna])
        matrizTransposta.append(linhaMatriz)
    return matrizTransposta

# Solicita ao usuário a quantidade de linhas e colunas para as matrizes
print("\033[1;44mOPERAÇÃO COM MATRIZES - TRANSPOSTA\033[m")

qtdLinhas = int(input("Digite a quantidade de linhas da Matriz A: "))
qtdColunas = int(input("Digite a quantidade de colunas da Matriz A: "))

print()
print("\033[1;41mCRIANDO A MATRIZ:\033[m ")
matriz_A = criaMatriz(qtdLinhas, qtdColunas)

print("\n\033[1;42mMATRIZ 'A' CRIADA\033[m")
imprimeMatriz(matriz_A)

print("\n\033[1;43mMATRIZ TRANSPOSTA:\033[m ")
imprimeMatriz(transposta(matriz_A))