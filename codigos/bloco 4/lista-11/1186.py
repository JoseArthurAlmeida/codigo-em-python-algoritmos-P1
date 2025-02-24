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


def abaixoDiagonalSecundaria(matriz):
    lista = []

    coluna = 0
    
    for i in range(len(matriz) - 1, 0, -1): # Começa da última linha
        for j in range(coluna + 1, len(matriz)):  # Começa da próxima coluna após a diagonal
            lista.append(matriz[i][j])
        coluna += 1
    
    return lista

def media(lista):
    return sum(lista) / len(lista)

if tipoOperacao == "S":
    print(sum(abaixoDiagonalSecundaria(matriz)))
else:
    print(f"{media(abaixoDiagonalSecundaria(matriz)):.1f}")








