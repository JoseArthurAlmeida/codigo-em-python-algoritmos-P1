# Para cada um dos códigos escreva a saída que será gerada.
def calculo(n1, n2):
    resultado = (n1 ** 3) / (n2 ** (1/3))
    # resultado = 27 / 3
    # resultado = 9
 
    print(n2) # 27
    n2 = 10
    print(n2) # 10

    return resultado

n1 = 3
n2 = 27
print(calculo(n1, n2)) # 9
print(n2) # 27