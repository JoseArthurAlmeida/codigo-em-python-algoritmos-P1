# 4. Crie uma função recursiva para calcular o valor mínimo e máximo em uma lista de números.
def valorMinMax(lista: list, min = None, max = None):
    if len(lista) == 0:
        return [min, max]
    
    primeiroEL = lista[0]
    
    if min == None or primeiroEL < min:
        min = primeiroEL
    if max == None or primeiroEL > max:
        max = primeiroEL
    
    return valorMinMax(lista[1:], min, max)

print(valorMinMax([-999, 233, 23, 0, 999]))
print(valorMinMax([-999]))