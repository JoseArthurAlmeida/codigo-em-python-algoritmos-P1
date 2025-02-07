def somaDigitos(numero):
    if numero < 10:
        return numero
    return somaDigitos(numero // 10) + numero % 10

print(somaDigitos(3)) # 3
print(somaDigitos(30)) # 3
print(somaDigitos(31)) # 4
print(somaDigitos(310)) # 4
print(somaDigitos(311)) # 5