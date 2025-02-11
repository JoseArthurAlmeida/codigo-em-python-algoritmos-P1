# import sys 
# print(sys.getrecursionlimit())

def fatorial(numero):
    resultado = 1
    for n in range(numero, 0, -1):
        resultado *= n
    return resultado

# print(fatorial(5)) # 120

def fatorialRecursivo(numero):
    if numero == 0:
        return 1
    return numero * fatorialRecursivo(numero - 1)

print(fatorialRecursivo(0))
print(fatorialRecursivo(1))
print(fatorialRecursivo(5))