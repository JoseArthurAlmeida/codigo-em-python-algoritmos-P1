# 6. Implemente uma função recursiva para calcular o MDC (máximo divisor comum) de dois números.
def mdc(a, b):
    if b == 0:
        return a
    else:
        return mdc(b, a % b)

print(mdc(2, 4))
print(mdc(100, 20))