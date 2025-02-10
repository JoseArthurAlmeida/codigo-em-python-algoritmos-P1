# 10. Desenvolva uma função recursiva para calcular o produto dos elementos de uma lista.

lista = [1, 1, 1, 2, 3, 2]

def produtoLista(lista):
    if len(lista) == 1:
        return lista[0]
    
    return lista[0] * produtoLista(lista[1:])

print(produtoLista(lista))