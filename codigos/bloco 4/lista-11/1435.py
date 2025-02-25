def criarMatriz(n):
    matriz = [[0] * n for _ in range(n)]

    # Preenche a matriz com 1 nas bordas
    for i in range(n):
        matriz[0][i] = 1  # Primeira linha
        matriz[i][0] = 1  # Primeira coluna
        matriz[n - 1][i] = 1  # Última linha
        matriz[i][n - 1] = 1  # Última coluna

    # Preenche o interior da matriz com valores crescentes
    for k in range(2, (n + 1) // 2 + 1):  # Começa em 2 e vai até a metade de n
        for i in range(k - 1, n - k + 1):
            for j in range(k - 1, n - k + 1):
                matriz[i][j] = k

    return matriz


def imprimir_matriz(matriz):
    for linha in matriz:
        print(" ".join(f"{x:3}" for x in linha))
    print()

while True:
    n = int(input())
    if n == 0:
        break

    matriz = criarMatriz(n)
    imprimir_matriz(matriz)