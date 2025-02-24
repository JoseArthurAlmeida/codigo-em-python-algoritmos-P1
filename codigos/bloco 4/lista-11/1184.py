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

def abaixoDiagonal(matriz):
    lista = []

    for i in range(len(matriz)):
        for j in range(i):
            lista.append(matriz[i][j])
    
    return lista
    
def media(lista):
    return sum(lista) / len(lista)

if tipoOperacao == "S":
    print(sum(abaixoDiagonal(matriz)))
else:
    print(f"{media(abaixoDiagonal(matriz)):.1f}")