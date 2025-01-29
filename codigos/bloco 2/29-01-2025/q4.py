# Escreva um código em Python que leia um inteiro positivo, n.
# Em seguida, deve-se gerar uma saída para cada número par no intervalo 2 até o número lido.
# O intervalo inclui os extremos 2 e n, caso este seja par.
# Caso contrário, finaliza em n-1.
# Cada saída deve estar em uma linha e, para cada uma delas, deve imprimir o número par corrente, i,
# seguido de dois pontos e a sequência de 1 até o i.
# Por exemplo, se a entrada for 11, a saída será: 
# 2: 1 2 
# 4: 1 2 3 4 
# 6: 1 2 3 4 5 6 
# 8: 1 2 3 4 5 6 7 8 
# 10: 1 2 3 4 5 6 7 8 9 10

n = int(input())

for i in range(2, n + 1, 2):
    # print(f"{i}: {" ".join(map(str, list(range(1, i + 1))))}")
    s = f"{i}: "
    for e in range(1, i + 1):
        s += f'{e} '
    print(s)