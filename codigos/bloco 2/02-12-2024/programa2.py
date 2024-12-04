import libMatematica
import libComandoTerminal

def showMenu():
    print("""--- CALCULADORA ---
    OPÇÕES:
        1. ADIÇÃO
        2. SUBTRAÇÃO
        3. MULTIPLICAÇÃO
        4. DIVISÃO
        5. SAIR""")

while True:
    libComandoTerminal.limpaTela()
    showMenu()
    
    opcao = int(input("Digite uma opção: "))
    
    if opcao == 5:
        libComandoTerminal.limpaTela()
        break
        
    else:
        if opcao not in [1, 2, 3, 4]:
            print("Opção inválida.")
            
        else:
            numero1 = int(input("Digite um número: "))
            numero2 = int(input("Digite um número: "))
            
            match opcao:
                case 1:
                    print(f"{numero1} + {numero2} = {libMatematica.adicao(numero1, numero2)}")
                case 2:
                    print(f"{numero1} - {numero2} = {libMatematica.subtracao(numero1, numero2)}")
                case 3:
                    print(f"{numero1} * {numero2} = {libMatematica.multiplicacao(numero1, numero2)}")
                case 4:
                    print(f"{numero1} / {numero2} = {libMatematica.divisao(numero1, numero2)}")
    input()
    libComandoTerminal.limpaTela()