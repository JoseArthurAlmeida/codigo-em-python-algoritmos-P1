# Converter se possivel os elementos de uma matriz para inteiros
from libMatriz import imprimeMatriz

def criaMatriz(linhas, colunas):
    # Cria uma matriz de tamanho 'linhas' x 'colunas' com valores fornecidos pelo usuário
    matriz = []
    for i in range(linhas):
        linha = []
        for j in range(colunas):
            linha.append(input(f"Digite o elemento da posição ({i + 1}, {j + 1}): "))
        matriz.append(linha)
    return matriz

def converterMatrizInteiro(matriz):
    matrizResultado = []
    for linha in matriz:
        linhaResultado = []
        for elemento in linha:
            if elemento.isnumeric():
                linhaResultado.append(int(elemento))
            else:
                linhaResultado.append(elemento)
        matrizResultado.append(linhaResultado)
    return matrizResultado

print("\033[1;44mEXERCÍCIO COM MATRIZES - VERIFICAR INTEIROS\033[m")

qtdLinhas = int(input("Digite a quantidade de linhas da Matriz A: "))
qtdColunas = int(input("Digite a quantidade de colunas da Matriz A: "))

print()
print("\033[1;41mCRIANDO A MATRIZ:\033[m ")
matriz_A = criaMatriz(qtdLinhas, qtdColunas)

print("\n\033[1;42mMATRIZ 'A' CRIADA\033[m")
imprimeMatriz(matriz_A)

print("\n\033[1;43mMATRIZ 'A' CONVERTIDA PARA INTEIROS:\033[m ")
imprimeMatriz(converterMatrizInteiro(matriz_A))