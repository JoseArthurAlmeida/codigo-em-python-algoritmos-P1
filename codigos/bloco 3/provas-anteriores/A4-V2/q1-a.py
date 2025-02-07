# Para cada um dos códigos escreva a saída que será gerada.
def calculo(n1, n2):
    resultado = n1 ** 3 + n2 ** (1/3)
 
    print(n1) # 3
    n1 = 10
    print(n1) # 10

    return resultado

x = 3
y = 27
print(calculo(x, y)) # 30.0
print(x) # 3