def minimo(lista):
    lista.sort()
    return lista[0]

def maximo(lista):
    lista.sort()
    return lista[-1]

x = []

for i in range(10):
    a = int(input())
    x.append(a)

print(min(x))
print(maximo(x))