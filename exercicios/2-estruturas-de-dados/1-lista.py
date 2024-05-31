# Crie uma lista apenas com elementos numéricos
lista_1 = [1, 11, 22, 4, 5, 10, 55, 60]
# Crie uma lista contendo todos os tipos e estrutura de dados que você aprendeu até agora
lista_2 = ['abacate', "feijão", 13, 3.14, 0, True, 3+4]
# Imprima na tela apenas os 5 primeiros elementos da lista
print (lista_1[:5])
print (lista_2[3:8])

# Crie um slice na lista para que imprima na tela os elementos de índice par
print (lista_1[0:-1:2])

# Remova da lista o último item
print (lista_1.pop())

# Insira na lista um novo item
print (lista_2.append(60))

# Remova da lista um item específico
print (lista_2.remove(3.14))

print (lista_1)
print (lista_2)