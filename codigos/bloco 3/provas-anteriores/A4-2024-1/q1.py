# Crie uma função em Python que irá receber uma string contendo uma fórmula contendo parênteses.
# A função deverá retornar True, caso os parênteses estejam inseridos corretamente, ou False, caso estejam incorretos.
# O importante é checar se os parênteses foram inseridos corretamente, o restante do conteúdo da fórmula deve ser ignorado.

def verificaParenteses(formula):
    contador = 0

    for caractere in formula:
        if caractere == "(":
            contador += 1
        elif caractere == ")":
            contador -= 1
            if contador < 0:
                return False
            
    return contador == 0

entrada = input("Digite uma formula: ")
print(f"{entrada} -> {verificaParenteses(entrada)}")