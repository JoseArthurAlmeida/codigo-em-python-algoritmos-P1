numero = int(input("Digite um número: "))

while numero != 0:

    ehPrimo = True

    if numero <= 1:
        ehPrimo = False

    for i in range(2, numero):
        if numero % i == 0:
            ehPrimo = False
            break

    if ehPrimo:
        print(f"O número {numero} é primo")
    else:
        print(f"O número {numero} não é primo")
    
    numero = int(input("Digite um número: "))

print("Acabou o programa")