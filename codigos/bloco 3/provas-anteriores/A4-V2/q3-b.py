# A série de Fibonacci tem 1 como primeiro e segundo elemento.
# A partir daí, a série segue definindo o próximo valor como a soma dos dois anteriores.
# Por exemplo, o terceiro elemento da série é 2 e o quarto é 3. Os oito primeiros elementos são 1, 1, 2, 3, 5, 8, 13 e 21.
# (b) Escreva uma nova implementação para a mesma função, só que desta vez a implementação deve ser recursiva. 

def fibonacci(numero):
    if numero <= 1:
        return numero
    
    return fibonacci(numero - 1) + fibonacci(numero - 2)

print(fibonacci(6))
print(fibonacci(8))