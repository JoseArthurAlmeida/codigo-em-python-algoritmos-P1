linhaOperacao = int(input())
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

def soma(matriz, linha):
    return sum(matriz[linha])

def media(matriz, linha):
    return soma(matriz, linha) / 12

if tipoOperacao == "S":
    print(soma(matriz, linhaOperacao))
else:
    print(f"{media(matriz, linhaOperacao):.1f}")