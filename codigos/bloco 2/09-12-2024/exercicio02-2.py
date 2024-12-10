import statistics

listaNumeros = []

for i in range(10):
    numero = int(input("Digite um número: "))
    listaNumeros.append(numero)
    
print(f"Lista ordenada = {sorted(listaNumeros)}")
print(f"Media = {statistics.mean(listaNumeros)}")
print(f"Mediana = {statistics.median(listaNumeros)}")
print(f"Moda = {statistics.mode(listaNumeros)}")