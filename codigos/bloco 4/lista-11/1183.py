tipoOperacao = input()

def criaMatriz(linhas, colunas):
    matriz = []
    for i in range(linhas):
        linha = []
        for j in range(colunas):
            linha.append(float(input())) # entrada
        matriz.append(linha)
    return matriz

matriz = criaMatriz(12, 12)

def acimaDiagonal(matriz):
    lista = []

    for i in range(len(matriz)):
        for j in range(i + 1, len(matriz[0])):  # Começa da próxima coluna após a diagonal
            lista.append(matriz[i][j])
    
    return lista
    
def media(lista):
    return sum(lista) / len(lista)

if tipoOperacao == "S":
    print(sum(acimaDiagonal(matriz)))
else:
    print(f"{media(acimaDiagonal(matriz)):.1f}")