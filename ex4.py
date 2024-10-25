# idade = int(input("Digite sua idade: "))

# ehMaiorDeIdade = idade >= 18

# if ehMaiorDeIdade:
#     print("Maior de Idade")
# else: 
#     print("Menor de Idade") 

numero1 = int(input("Digite um número: "))
numero2 = int(input("Digite um número: "))
numero3 = int(input("Digite um número: "))

maior = numero1 # assumo que o 1º é o maior

if maior < numero2:
    maior = numero2

if maior < numero3: 
    maior = numero3

print(f"1º Solução => O maior é: {maior}")

# 2º Solução
print(f"2º Solução => O maior é: {max(numero1, numero2, numero3)}")