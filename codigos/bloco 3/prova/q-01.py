def Atanalva(n, seq = 1000):
    if n == 1:
        return seq
    elif n > 54:
        return "Não existe"
    else:
        if (n % 2) == 0:
            return Atanalva(n -1, seq - 50)
        else:
            return Atanalva(n-1, seq - 25)

print(Atanalva(1))
print(Atanalva(2))
print(Atanalva(3))
print(Atanalva(4))
print(Atanalva(5))
print(Atanalva(6))
print(Atanalva(7))
print(Atanalva(54))