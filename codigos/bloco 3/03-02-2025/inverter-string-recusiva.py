# Slicing Strings
# string[inicio<0>:fim<0>:passo<1>]

def inverter(palavra):
    return palavra[::-1]

def inverterRec(palavra):
    if len(palavra) == 1:
        return palavra
    
    return inverterRec(palavra[1:]) + palavra[0]

print(inverterRec("Amor")) # romA