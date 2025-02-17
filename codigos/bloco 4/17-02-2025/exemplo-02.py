def criaMatriz(linhas, colunas):
    matriz = []
    for i in range(linhas):
        linha = []
        for j in range(colunas):
            linha.append(int(input(f"Digite o elemento da posição ({i + 1}, {j + 1}): ")))
        matriz.append(linha)
    return matriz

def somaMatrizes(matriz_1, matriz_2, linhas, colunas):
    matriz = []
    for i in range(linhas):
        linha = []
        for j in range(colunas):
            linha.append(matriz_1[i][j] + matriz_2[i][j])
        matriz.append(linha)
    return matriz

def imprimeMatriz(matriz):
    for linha in matriz:
       print(linha)

qtdLinhas = int(input("Digite a quantidade de linhas: "))
qtdColunas = int(input("Digite a quantidade de colunas: "))

print()
print("CRIANDO A MATRIZ 1: ")
matriz_A = criaMatriz(qtdLinhas, qtdColunas)

print()
print("CRIANDO A MATRIZ 2: ")
matriz_B = criaMatriz(qtdLinhas, qtdColunas)

soma = somaMatrizes(matriz_A, matriz_B, qtdLinhas, qtdColunas)
imprimeMatriz(soma)