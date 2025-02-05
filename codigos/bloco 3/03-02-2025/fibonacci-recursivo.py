def fibonacci(quantidade):
    fibonacci = [0, 1]

    for i in range(2, quantidade):
        soma = fibonacci[i - 1] + fibonacci[i - 2]
        fibonacci.append(soma)
    
    return fibonacci[quantidade - 1]

def fibonacciRecursivo(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2) 

print(fibonacci(45)) # 5
# print(fibonacci(6)) # 8
# print(fibonacci(2)) # 1