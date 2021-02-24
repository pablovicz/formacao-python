idades = [21, 45, 34, 65, 25, 57, 35]

for i in range(len(idades)):
    print(i, idades[i])

## Enumerate

for idade in enumerate(idades):
    print(idade)


## Sorted - ordena in place
print(sorted(idades)) # crescente

print(sorted(idades, reverse=True)) # descendente


## Sort
idades.sort()  # vai ordenar o objeto lista - altera a lista original
print(idades)



