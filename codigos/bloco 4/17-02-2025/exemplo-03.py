matriz_1 = []
matriz_2 = []

qtdLinhas = int(input("Digite a quantidade de linhas: "))
qtdColunas = int(input("Digite a quantidade de colunas: "))


for e in range(qtdLinhas):
    linha = list(map(int, input(f"Digite os valores da linha {e + 1} da matriz 1: ").split()))
    matriz_1.append(linha)

for e in range(qtdLinhas):
    linha = list(map(int, input(f"Digite os valores da linha {e + 1} da matriz 2: ").split()))
    matriz_2.append(linha)

matriz_3 = []

for i in range(qtdLinhas):
    linha = []
    for j in range(qtdColunas):
        linha.append(matriz_1[i][j] + matriz_2[i][j])
    matriz_3.append(linha)

for linha in matriz_3:
    for elemento in linha:
        print(elemento, end= " ")
    print()