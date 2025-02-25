def quadradoMatriz(matriz):
    return [[elemento ** 2 for elemento in linha] for linha in matriz]

def formatarMatriz(matriz):
    # Encontrar o maior número de dígitos em cada coluna
    colunas = len(matriz[0])
    larguras = [max(len(str(linha[i])) for linha in matriz) for i in range(colunas)]
    
    # Formatar cada linha da matriz
    for linha in matriz:
        elementos_formatados = []
        for i, elemento in enumerate(linha):
            elementos_formatados.append(f"{elemento:>{larguras[i]}}")
        print(" ".join(elementos_formatados))

def criaMatriz(linhas):
    matriz = []
    for i in range(linhas):
        matriz.append(list(map(int, input().split())))
    return matriz

# Leitura da entrada
N = int(input())
for x in range(4, 4 + N):
    M = int(input())
    matriz = criaMatriz(M)
    
    quadrado_matriz = quadradoMatriz(matriz)
    
    print(f"Quadrado da matriz #{x}:")
    formatarMatriz(quadrado_matriz)
    if x < 3 + N:  # Adicionar linha em branco entre matrizes, exceto após a última
        print()