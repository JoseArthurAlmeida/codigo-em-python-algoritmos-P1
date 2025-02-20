# Escreva uma função que verifique se uma matriz N x N é simétrica (ou seja, igual à sua transposta).
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

def simetrica(matriz_1, matriz_2):
    return matriz_1 == matriz_2

# Solicita ao usuário a quantidade de linhas e colunas para as matrizes
print("\033[1;44mOPERAÇÃO COM MATRIZES - SIMÉTRICA\033[m")

qtdLinhas = int(input("Digite a quantidade de linhas da Matriz A: "))
qtdColunas = int(input("Digite a quantidade de colunas da Matriz A: "))

print()
print("\033[1;41mCRIANDO A MATRIZ:\033[m ")
matriz_A = criaMatriz(qtdLinhas, qtdColunas)

print("\n\033[1;42mMATRIZ 'A' CRIADA\033[m")
imprimeMatriz(matriz_A)

matrizTransposta_A = transposta(matriz_A)

if simetrica(matriz_A, matrizTransposta_A):
    print("A matriz informada é simétrica")
else:
    print("A matriz informada não é simétrica")