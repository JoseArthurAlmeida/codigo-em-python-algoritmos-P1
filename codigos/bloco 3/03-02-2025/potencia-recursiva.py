def potencia(x, y):
    return x ** y

# print(potencia(2, 3))

def potenciaRecursiva(x, y):
    if y == 0:
        return 1
    return x * potenciaRecursiva(x, y -1) 

print(potenciaRecursiva(2, 0))
print(potenciaRecursiva(2, 1))
print(potenciaRecursiva(2, 2))