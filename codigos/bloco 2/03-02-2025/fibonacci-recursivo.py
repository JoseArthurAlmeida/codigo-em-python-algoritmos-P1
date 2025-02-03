def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2) 

print(fibonacci(5)) # 5
print(fibonacci(6)) # 8
print(fibonacci(2)) # 1