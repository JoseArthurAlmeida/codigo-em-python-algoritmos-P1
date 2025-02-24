matriz_A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

matriz_B = matriz_A.copy()

def imprimeMatriz(matriz):
    for linha in matriz:
        print(linha)

print("Matriz A:")
imprimeMatriz(matriz_A)
print()
print("Matriz B:")
imprimeMatriz(matriz_B)

def copiarMatriz(matriz):
   return [linha[:] for linha in matriz]

matriz_C = copiarMatriz(matriz_A)
print()
print("Matriz C:")
imprimeMatriz(matriz_C)