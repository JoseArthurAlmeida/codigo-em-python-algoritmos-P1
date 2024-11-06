# for i in range(101):
#     if (i % 2) != 0:
#         print(i)

# for i in range(5):
#     numero = int(input(f"{i + 1}. Digite um número: "))
#     if (numero % 2) == 0:
#         print(f"O número {numero} é par")
#     else:
#         print(f"O número {numero} é impar")

quantidadeVezes = int(input("Digite a qtde. de vezes: "))

for i in range(quantidadeVezes):
    numero = int(input(f"{i + 1}. Digite um número: "))
    if (numero % 2) == 0:
        print(f"O número {numero} é par")
    else:
        print(f"O número {numero} é impar")