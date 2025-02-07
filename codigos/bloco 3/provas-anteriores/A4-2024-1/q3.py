# Crie uma função em Python que recebe uma string como parâmetro e retorna True se a string for um palíndromo, ou False, caso contrário.
# Um palíndromo é uma palavra, frase ou sequência de caracteres que permanece a mesma quando lida de trás para frente.
# A função deve ignorar maiúsculas e minúsculas.

def ehPalindromo(palavra):
    palavra = palavra.lower()
    palavraInvertida = palavra[:: -1]
    print(palavraInvertida)
    return palavra == palavraInvertida

print(ehPalindromo("arara"))
print(ehPalindromo("uno"))
print(ehPalindromo("ovo"))