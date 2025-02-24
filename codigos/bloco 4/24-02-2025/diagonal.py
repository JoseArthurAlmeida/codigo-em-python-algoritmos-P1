from libMatriz import imprimeMatriz

# Substitui os elementos da diagonal principal por 0
def substituiDiagonalPrincipal(matriz):
    for i in range(len(matriz)):
       matriz[i][i] = 0

# Substitui os elementos da diagonal secundária por 0
def substituiDiagonalSecundaria(matriz):
    for i in range(len(matriz)):
       matriz[i][len(matriz) -1 - i] = 0

# Zera os elementos acima da diagonal principal
def zerarDiagSuperior(matriz):
    for i in range(len(matriz)):
        for j in range(i + 1, len(matriz[0])):  # Começa da próxima coluna após a diagonal
            matriz[i][j] = 0
    
    return matriz

# Zera os elementos abaixo da diagonal principal
def zerarDiagInferior(matriz):
    for i in range(len(matriz)):
        for j in range(i):  # Começa da próxima coluna após a diagonal
            matriz[j][i] = 0
    
    return matriz

# Zera os elementos acima da diagonal secundária
def zerarDiagSecundariaSuperior(matriz):
    nova_matriz = [linha[:] for linha in matriz]  # Cria uma cópia da matriz

    coluna = len(nova_matriz) - 1
    
    for i in range(len(nova_matriz)):
        for j in range(coluna - 1, -1, -1):  # Começa da próxima coluna após a diagonal
            nova_matriz[i][j] = 0
        coluna -= 1
    
    return nova_matriz

# Zera os elementos abaixo da diagonal secundária
def zerarDiagSecundariaInferior(matriz):
    nova_matriz = [linha[:] for linha in matriz]  # Cria uma cópia da matriz
    
    coluna = 0
    
    for i in range(len(nova_matriz) - 1, 0, -1):
        for j in range(coluna + 1, len(nova_matriz)):  # Começa da próxima coluna após a diagonal
            nova_matriz[i][j] = 0
        coluna += 1
    
    return nova_matriz