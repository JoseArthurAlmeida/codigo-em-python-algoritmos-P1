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

def acimaDiagonalSecundaria(matriz):
    lista = []
    
    coluna = len(matriz) - 1
    
    for i in range(len(matriz)):
        for j in range(coluna - 1, -1, -1):  # Começa da próxima coluna após a diagonal
            lista.append(matriz[i][j]) 
        coluna -= 1
    
    return lista

def media(lista):
    return sum(lista) / len(lista)

if tipoOperacao == "S":
    print(sum(acimaDiagonalSecundaria(matriz)))
else:
    print(f"{media(acimaDiagonalSecundaria(matriz)):.1f}")