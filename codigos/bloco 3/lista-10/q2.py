# 2. Crie uma função recursiva que verifique se uma string é um palíndromo.
entrada = input().lower()

# def inverterString(palavra):
#     if len(palavra) == 1:
#         return palavra
    
#     return inverterString(palavra[1:]) + palavra[0]

# def ehPalindromo(palavra):
#     return inverterString(palavra) == palavra

def ehPalindromo(palavra):

    if len(palavra) <= 1:
        return True
    
    if palavra[0] == palavra[-1]:
        return ehPalindromo(palavra[1:-1])
    else:
        return False

print(ehPalindromo(entrada))