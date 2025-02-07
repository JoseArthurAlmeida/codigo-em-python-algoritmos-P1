# Dizemos que um número natural é triangular se ele é produto de três números naturais consecutivos.
# Exemplo: 120 é triangular, pois 4 x 5 x 6 = 120. Implemente uma função que indica se um número é triangular ou não.
# Em seguida escreva um programa que leia números inteiros e indique se é triangular ou não, usando a função.
# O programa deve ser encerrado quando a entrada for 0

def ehTriangular(num):
    for i in range(num):
        if (i * (i + 1) * (i + 2)) == num:
            return True
        
    return False

numero = int(input("Digite um inteiro: "))
while numero != 0:
    print(f"O número {numero} {"é tringular" if ehTriangular(numero) else "não é triangular"}")
    numero = int(input("Digite um inteiro: "))

print("O programa encerrou.")