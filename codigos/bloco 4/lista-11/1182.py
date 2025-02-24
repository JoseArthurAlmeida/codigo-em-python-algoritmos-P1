colunaOperacao = int(input())
tipoOperacao = input()

def criaMatriz(linhas, colunas):
    matriz = []
    for i in range(linhas):
        linha = []
        for j in range(colunas):
            linha.append(float(input()))
        matriz.append(linha)
    return matriz

matriz = criaMatriz(12, 12)

def soma(matriz, coluna):
    colunaTemp = []

    for indiceLinha in range(len(matriz)):
        colunaTemp.append(matriz[indiceLinha][coluna])

    return sum(colunaTemp)

def media(matriz, coluna):
    return soma(matriz, coluna) / 12

if tipoOperacao == "S":
    print(soma(matriz, colunaOperacao))
else:
    print(f"{media(matriz, colunaOperacao):.1f}")