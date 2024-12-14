listaIdades = [18, 0, 45, 56]
listaIdades.append(23) # Adiciona no final
print(listaIdades) # Saída: [18, 0, 45, 56, 23]

print(type(listaIdades)) # <class 'list'>
print(len(listaIdades)) # Saída: 5. Retorna a quantidade de elementos na lista 

novasIdades = [30, 35]
listaIdades.extend(novasIdades) # Estende a lista, adicionando todos os elementos de outro iterável (como outra lista).
print(listaIdades)  # Saída: [18, 0, 45, 56, 23, 30, 35]

listaIdades.insert(2, 20) # Insere um item em uma posição específica
print(listaIdades)  # Saída: [18, 0, 20, 45, 56, 23, 30, 35]

listaIdades.remove(0) # Remove o primeiro item com o valor especificado.
print(listaIdades)  # Saída: [18, 20, 45, 56, 23, 30, 35]

ultimaIdade = listaIdades.pop() # Remove o item em uma posição específica e o retorna. Se nenhum índice for especificado, remove e retorna o último item.
print(ultimaIdade)  # Saída: 35
print(listaIdades)  # Saída: [18, 20, 45, 56, 23, 30]

indice_45 = listaIdades.index(45) # Retorna o índice da primeira ocorrência de um valor.
print(indice_45)  # Saída: 2

contagem_23 = listaIdades.count(23) # Retorna o número de ocorrências de um valor.
print(contagem_23)  # Saída: 1

listaIdades.sort() # Ordena os elementos da lista em ordem crescente.
print(listaIdades) # Saída: [18, 20, 23, 30, 45, 56]

listaIdades.reverse() # Inverte a ordem dos elementos da lista.
print(listaIdades)  # Saída: [56, 45, 30, 25, 20, 18]

listaIdades.clear() # Remove todos os elementos da lista.
print(listaIdades)  # Saída: []