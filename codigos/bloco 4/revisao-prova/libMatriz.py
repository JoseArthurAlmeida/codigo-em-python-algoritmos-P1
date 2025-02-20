def criaMatriz(linhas, colunas):
    # Cria uma matriz de tamanho 'linhas' x 'colunas' com valores fornecidos pelo usuário
    matriz = []
    for i in range(linhas):
        linha = []
        for j in range(colunas):
            linha.append(int(input(f"Digite o elemento da posição ({i + 1}, {j + 1}): ")))
        matriz.append(linha)
    return matriz

def imprimeMatriz(matriz):
    # Imprime a matriz no console
    for linha in matriz:
       print(linha)