# 3. Desenvolva uma função recursiva que conte o número de ocorrências de um caractere específico em uma string.
entrada = input("Digite uma string: ")
caractereIN = input("Digite um caractere: ")

def contarCaractere(string, caractere):
    if len(string) == 0:
        return 0
    
    if string[0] == caractere:
        return 1 + contarCaractere(string[1:], caractere)

    return contarCaractere(string[1:], caractere)

print(contarCaractere(entrada, caractereIN))