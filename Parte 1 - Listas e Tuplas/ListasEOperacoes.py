# List
## listas em python podem ser alteradas
## valores podem ser adicionados ao final dela, excluidos, alterados, etc
## documentacao - https://docs.python.org/3/tutorial/datastructures.html

## inicializando lista
idades = [39, 30, 27, 18, 15]

def print_list(lista):
    print('---------------')
    index = 0
    for item in lista:
        print(f'Lemento {index}: {item}')
        index += 1
    print('---------------')

# adicionando valor no final da lista
idades.append(50)
idades.append(50)
print_list(idades)

# adicionando valor em uma posicao especifica da lista
idades.insert(3, 5) # insere a idade 5 na posicao 3
print_list(idades)


# criando outra list a partir de uma existente
idades_no_ano_que_vem = [(idade + 1) for idade in idades]
print_list(idades_no_ano_que_vem)


# removendo valores da lista  - remove apenas a primeira aparição do elemento
idades.remove(50)
print_list(idades)

# conferindo se valor existe em lista
print(28 in idades) #False
print(50 in idades) #True

# inserindo mais de um elemento
idades.extend([13, 14])
print_list(idades)


# filtrando listas
print_list([(idade) for idade in idades if idade > 21])

