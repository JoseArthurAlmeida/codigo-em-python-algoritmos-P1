import datetime
hoje = datetime.datetime.now()
ano = hoje.year

nome = input("Digite seu nome: ")
# idade = input("Digite sua idade: ")
sexo = input("Digite seu sexo [M / F / O]: ")
anoDeNascimento = int(input("Digite o seu ano de nascimento: "))

idade = ano - anoDeNascimento 

idadeTipo = ""

if idade % 2 == 0:
    idadeTipo = "Par"
else:
    idadeTipo = "Impar"

ehBissexto = ""

if anoDeNascimento % 4 == 0:
    ehBissexto = "é bissexto"
else:
    ehBissexto = "não é bissexto"

if sexo in "F f":
    print(f"""Olá, {nome}! é uma mulher de {idade} anos.
Sua idade eh {idadeTipo}
O ano de nascimento {ehBissexto}""")
elif sexo in "M m":
    print(f"""Olá, {nome}! é um homem de {idade} anos
Sua idade eh {idadeTipo}
O ano de nascimento {ehBissexto}""")
    
elif sexo in "O o":
    print(f"""Olá, {nome}! não se identifica com M ou F e tem {idade} anos
Sua idade eh {idadeTipo}
O ano de nascimento {ehBissexto}""")