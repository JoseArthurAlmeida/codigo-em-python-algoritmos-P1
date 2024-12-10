def calcular_moda(lista):
    frequencias = {}
    
    for num in lista:
        if num in frequencias:
            frequencias[num] += 1
        else:
            frequencias[num] = 1

    max_frequencia = max(frequencias.values())
    
    for num in frequencias:
        if frequencias[num] == max_frequencia:
            return num
    
numeros = [2, 3, 2, 8, 5, 2, 9, 7, 5, 2]
resultado = calcular_moda(numeros)
print("A moda(s) é(são):", resultado)