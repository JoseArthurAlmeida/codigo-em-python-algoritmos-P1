# 12. Desenvolva uma função recursiva para imprimir uma lista de trás para frente.
lista = [1, 2, 4, 5, 6]

# execução das funções recursivas partem do princípio de pilha, onde a primeira chamada é a última a ser retornada
def listaTrasFrente(lista):
    if len(lista) == 0:
        return
    
    listaTrasFrente(lista[1:])
    print(lista[0])

listaTrasFrente(lista)