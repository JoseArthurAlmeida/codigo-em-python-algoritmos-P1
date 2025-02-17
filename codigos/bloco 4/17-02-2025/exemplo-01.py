e1 = int(input())
e2 = int(input())
e3 = int(input())
e4 = int(input())

matriz = [[e1, e2], [e3, e4]]

for linha in matriz:
    for elemento in linha:
        print(elemento, end= " ")
    print()

matriz_2x3 = [
    [3, 3, 2],
    [3, 3, 2]
]

for linha in matriz_2x3:
    for elemento in linha:
        print(elemento ** 2, end= " ")
    print()
