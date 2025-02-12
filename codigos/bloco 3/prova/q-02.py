def verificaZero(num):
    if num == 0:
        return 10
    else:
        return num

def trocaPeloAnterior(numero):
    numero = str(numero)
    if len(numero) == 1:
        return str(verificaZero(int(numero[0])) - 1)
    
    primeiroNumero = numero[0]
    primeiroNumero = verificaZero(int(primeiroNumero))

    return str(primeiroNumero - 1) + str(trocaPeloAnterior(numero[1:]))

print(trocaPeloAnterior(203))