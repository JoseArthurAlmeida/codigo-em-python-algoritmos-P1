import random

opcaoEscolhida = 0

while opcaoEscolhida != 3:
    entrada = input("Digite 'CARA' ou 'COROA': ").lower()
    parar = False
    
    if entrada == "cara":
        opcaoEscolhida = 1
        
    elif entrada == "coroa":
        opcaoEscolhida = 2
        
    elif entrada == "parar":
        opcaoEscolhida = 3
        parar = True
        
    else:
        print("Opção Inválida")
        parar = True
        
    if not parar:
        numeroAleatorio = random.randint(1, 2)
        
        if opcaoEscolhida == numeroAleatorio:
            print("Você Ganhou")
        else:
            print("Você Perdeu")
        
        