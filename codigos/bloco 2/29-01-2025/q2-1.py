# 2. Digamos que não existam as funções min, max.
# Escreva as implementações das funções min e max. Faça duas versões de cada (com e sem sort). (20 pontos) 

def minimo(lista):
    m = lista[0]
    for e in lista[1:]:
        if e < m:
            m = e    
    return m

x = []

def maximo(lista):
    m = lista[0]
    for e in lista[1:]:
        if e > m:
            m = e
    return m

for i in range(10):
    a = int(input())
    x.append(a)

print(minimo(x))
print(maximo(x))