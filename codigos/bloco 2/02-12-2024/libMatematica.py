def adicao(num1, num2):
    return num1 + num2
    
def subtracao(num1, num2):
    return num1 - num2
    
def multiplicacao(num1, num2):
    return num1 * num2
    
def divisao(num1, num2):
    return num1 / num2
    
def primo(num):
    if num <= 1:
        return False
        
    for i in range(2, num):
        if num % i == 0:
            return False
    
    return True

def fatorial(num):
    calculo = 1
    
    for i in range(1, num + 1):
        calculo *= i
        
    return calculo
    
def quadrado(num):
    return num * num