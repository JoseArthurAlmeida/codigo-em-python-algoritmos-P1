# 15. Desenvolva uma função recursiva para determinar se uma sequência de parênteses é válida.
def verificaParenteses(sequencia, cont = 0):
    if cont < 0:
        return False
    
    if sequencia:
        if sequencia[0] == "(":
            return verificaParenteses(sequencia[1:], cont + 1)
        elif sequencia[0] == ")":
          return verificaParenteses(sequencia[1:], cont - 1)
        
    return cont == 0
    
print(verificaParenteses("()")) # True
print(verificaParenteses("()()")) # True
print(verificaParenteses(")(")) # False
print(verificaParenteses("(((((()))")) # False