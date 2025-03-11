# Criando um dicionário V.1
carro = {"fabricante": "Volks", "modelo": "Fusca", "ano": 1984}
print(carro)

# Acessando um valor
print(carro["modelo"])

# Alterando um valor
carro["ano"] = 1980
print(carro)

# Adicionando um novo par chave-valor
carro["cor"] = "azul"
print(carro)

# Removendo um par chave-valor
del carro["ano"]
print(carro)

print()

# Criando um dicionário V.2
carro = dict(fabricante="Ford", modelo="Del Rey", ano=1986)
print(carro)

# Acessando um valor
print(carro.get("modelo"))

# Alterando um valor
carro.update({"ano": 1985})
print(carro)

# Adicionando um novo par chave-valor
carro.update({"cor": "preto"})
print(carro)

# Removendo um par chave-valor
carro.pop("ano")
print(carro)
