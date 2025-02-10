# 9. Crie uma função recursiva para determinar se uma lista está ordenada.
def isListaOrdenada(lista):
    if len(lista) <= 1:
        return True
    if lista[0] > lista[1]:
        return False
    return isListaOrdenada(lista[1:])

print(isListaOrdenada([]))
print(isListaOrdenada([1, 2, 3, 4, 4, 4.0000000000000000001, 5]))
print(isListaOrdenada([1, 2, 3, 400000000, 4, 4, 5]))