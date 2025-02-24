def copiaMatriz(matriz):
    copia = []
    linhas = len(matriz)
    colunas = len(matriz[0])
    for i in range(linhas):
        linha = []
        for j in range(colunas):
            linha.append(matriz[i][j])
        copia.append(linha)
    return copia

matrixA = [[1,2,3],[4,5,6],[7,8,9]]
matrixB = copiaMatriz(matrixA)

def transpostaMatriz(matriz):
    transposta = matriz
    copia = copiaMatriz(matriz)
    linhas = len(matriz)
    colunas = len(matriz[0])
    for i in range(linhas):
        for j in range(colunas):
            transposta[i][j] = copia[j][i]
    return transposta

print("### MATRIZ A:")
for linha in matrixA:
    print(linha)

print()

tranp = transpostaMatriz(matrixA)

print("### MATRIZ TRANSPOSTA:")
for linha in tranp:
    print(linha)