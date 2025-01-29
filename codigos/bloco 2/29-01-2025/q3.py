# Escreva um código em Python que leia um inteiro, representando um valor a ser sacado, e em seguida,
# escreva o número de cada uma das notas que o caixa eletrônico deve entregar.
# O menor número (total) de notas deve ser entregue, só há disponibilidade de notas de 50 e de 20 reais e um número bem restrito de notas de 50, apenas 2.
# Caso o valor não seja possível de ser entregue integralmente, deve ser apresentada uma mensagem informativa da situação. (30 pontos) 

valor = int(input())

notas50 = 0
notas20 = 0

if valor < 50 and valor not in [20, 40]:
    print("Valor não disponível!")
elif valor >= 50 and  (valor % 10) != 0: # Não considerar valores não representaveis (1, 2, 3, 4, 5, 6, 7, 8, 9)
    print("Valor não disponível!")
else:
    if valor <= 100:
        if valor in [60, 80]:
            notas20 = valor // 20
        else:
            notas50 = valor // 50
            notas20 = (valor - notas50 * 50) // 20
    else:
        if (valor // 10) % 2 != 0:
            notas50 = 1
            notas20 = (valor - notas50 * 50) // 20
        else:
            notas50 = valor // 50
            if notas50 > 2:
                notas50 = 2
            notas20 = (valor - notas50 * 50) // 20
    
    print(f"{notas50} notas de R$ 50")
    print(f"{notas20} notas de R$ 20")