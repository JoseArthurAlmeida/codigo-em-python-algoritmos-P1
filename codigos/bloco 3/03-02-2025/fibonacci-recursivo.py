def fibonacci(n):
    fibonacci = [0, 1]

    for i in range(2, n + 1):
        soma = fibonacci[i - 1] + fibonacci[i - 2]
        fibonacci.append(soma)
    
    return fibonacci[n]

def fibonacciRecursivo(n):
    if n <= 1:
        return n
    return fibonacciRecursivo(n - 1) + fibonacciRecursivo(n - 2) 

# 0 ,1, 1, 2, 3, 5, 8, 13
print("Fibonacci recursivo")
print(fibonacciRecursivo(0))
print(fibonacciRecursivo(1))
print(fibonacciRecursivo(2))
print(fibonacciRecursivo(3))

print("Fibonacci")
print(fibonacci(0))
print(fibonacci(1))
print(fibonacci(2))
print(fibonacci(3))