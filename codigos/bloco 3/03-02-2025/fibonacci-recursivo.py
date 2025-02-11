def fibonacci(quantidade):
    fibonacci = [0, 1]

    for i in range(2, quantidade + 1):
        soma = fibonacci[i - 1] + fibonacci[i - 2]
        fibonacci.append(soma)
    
    return fibonacci[quantidade]

def fibonacciRecursivo(n):
    if n <= 1:
        return n
    return fibonacciRecursivo(n - 1) + fibonacciRecursivo(n - 2) 
# 0 ,1, 1, 2, 3, 5, 8, 13
print(fibonacciRecursivo(3))