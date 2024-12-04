import libMatematica
import libComandoTerminal

def showMenu():
    print("""--- MENU ---
    OPÇÕES:
        1. Verificar se é primo
        2. Calcular fatorial
        3. Calcular o quadrado do número
        4. SAIR""")

while True:
    libComandoTerminal.limpaTela()
    showMenu()
    
    opcao = int(input("Digite uma opção: "))
    
    if opcao == 4:
        libComandoTerminal.limpaTela()
        break
        
    else:
        if opcao not in [1, 2, 3]:
            print("Opção inválida.\nPressione ENTER para escolher uma opção válida")
        else:
            numero = int(input("Digite um número: "))

    match opcao:
        case 1:
            print(f"O número {numero} é {"primo" if libMatematica.primo(numero) else "não é primo"}\nPressione ENTER para usar denovo")
        case 2:
            print(f"{numero}! = {libMatematica.fatorial(numero)}\nPressione ENTER para usar denovo")
        case 3:
            print(f"{numero} ** 2 = {libMatematica.quadrado(numero)}\nPressione ENTER para usar denovo")

    input()
    libComandoTerminal.limpaTela()