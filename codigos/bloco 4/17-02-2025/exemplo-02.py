def criaMatriz(linhas, colunas):
    # Cria uma matriz de tamanho 'linhas' x 'colunas' com valores fornecidos pelo usuário
    matriz = []
    for i in range(linhas):
        linha = []
        for j in range(colunas):
            linha.append(int(input(f"Digite o elemento da posição ({i + 1}, {j + 1}): ")))
        matriz.append(linha)
    return matriz

def somaMatrizes(matriz_1, matriz_2, linhas, colunas):
    # Soma duas matrizes de mesmo tamanho e retorna a matriz resultante
    matriz = []
    for i in range(linhas):
        linha = []
        for j in range(colunas):
            linha.append(matriz_1[i][j] + matriz_2[i][j])
        matriz.append(linha)
    return matriz

def imprimeMatriz(matriz):
    # Imprime a matriz no console
    for linha in matriz:
       print(linha)

# Solicita ao usuário a quantidade de linhas e colunas para as matrizes
qtdLinhas = int(input("Digite a quantidade de linhas: "))
qtdColunas = int(input("Digite a quantidade de colunas: "))

print()
print("CRIANDO A MATRIZ 1: ")
# Cria a primeira matriz com os valores fornecidos pelo usuário
matriz_A = criaMatriz(qtdLinhas, qtdColunas)

print()
print("CRIANDO A MATRIZ 2: ")
# Cria a segunda matriz com os valores fornecidos pelo usuário
matriz_B = criaMatriz(qtdLinhas, qtdColunas)

soma = somaMatrizes(matriz_A, matriz_B, qtdLinhas, qtdColunas)
imprimeMatriz(soma)