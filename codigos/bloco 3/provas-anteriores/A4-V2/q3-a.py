# A série de Fibonacci tem 1 como primeiro e segundo elemento.
# A partir daí, a série segue definindo o próximo valor como a soma dos dois anteriores.
# Por exemplo, o terceiro elemento da série é 2 e o quarto é 3. Os oito primeiros elementos são 1, 1, 2, 3, 5, 8, 13 e 21. 
# (a) Escreva uma função que receba um número inteiro, i, e retorne o i-ésimo elemento da série.
# Por exemplo, se o i recebido for 6 o retorno deve ser 8 ou se o i recebido for 8 o retorno deve ser 21.
# Escreva uma função não recursiva.

def fibonacci(indice):
    fibo = [1, 1]
    for i in range(2, indice + 1):
        elemento = fibo[i - 1] + fibo[i - 2]
        fibo.append(elemento)
    
    return fibo[indice - 1]

print(fibonacci(6))
print(fibonacci(8))