# numero = int(input("Digite um número: "))

# while numero != 0:
#     print(f"Número digitado = {numero}")
#     numero = int(input("Digite um número: "))
nome = ""
idade = 0
sexo = ""

while idade <= 50:
    nome = input("Digite seu nome: ")
    idade = int(input("Digite seu idade: "))
    sexo = input("Digite seu sexo: ")
    print(f"Nome: {nome}, Idade: {idade}, Sexo: {sexo} \n")