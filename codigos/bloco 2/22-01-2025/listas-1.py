# - SOLICITA AO USUÁRIO 10 NÚMEROS
# - INSERE EM LISTA
import statistics

listaNumeros = []
for i in range(10):
    listaNumeros.append(int(input("Digite um número: ")))

# - MOSTRA EM ORDEM CRESCENTE
listaNumeros.sort()
print(f"Ordem crescente: {listaNumeros}")

# - MOSTRA EM ORDEM DECRESCENTE
listaNumeros.reverse()
print(f"Ordem decrescente: {listaNumeros}")

# - MOSTRA MEDIA, MEDIANA E MODA

print(f"Media = {statistics.mean(listaNumeros)}")
print(f"Mediana = {statistics.median(listaNumeros)}")
print(f"Moda = {statistics.mode(listaNumeros)}")

# - REMOVE OS ELEMENTOS QUE MAIS SE REPETEM
listaNumeros = list(filter(lambda elemento: listaNumeros.count(elemento) == 1, listaNumeros))
print(f"Sem elementos que mais se repetem: {listaNumeros}")

# - REMOVER OS 3 MENORES ELEMENTOS
for i in range(3):
    listaNumeros.remove(min(listaNumeros))

print(f"Sem os 3 menores elementos: {listaNumeros}")

# - REMOVER OS 4 MAIORES ELEMENTOS
for i in range(4):
    listaNumeros.remove(max(listaNumeros))
print(f"Sem os 4 maiores elementos: {listaNumeros}")