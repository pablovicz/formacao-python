

usuarios_data_science = [15, 23, 43, 56]
usuarios_machine_learning = [13, 23, 56, 42]


assistiram = usuarios_data_science.copy()
assistiram.extend(usuarios_machine_learning)

print(assistiram)

# ignorando elementos em comum
# conjunto - "lista" com elementos unicos
### conjuntos perder a indexacao dos elementos

print(set(assistiram))


# operações com conjuntos

conjunto_data_science = set(usuarios_data_science)
conjunto_machine_learning = set(usuarios_machine_learning)

# uniao
print("União: ", conjunto_machine_learning | conjunto_data_science)

# intersecção
print("Intersecção: ", conjunto_machine_learning & conjunto_data_science)

# diferença
print("Diferença: ", conjunto_data_science - conjunto_machine_learning)

# Ou exclusivo
print("Ou Exclusivo: ", conjunto_data_science ^ conjunto_machine_learning)


# Adicionando elementos

conjunto_machine_learning.add(10)
print(conjunto_machine_learning)

# Conjunto congelado
## nao permite alteracoes

frozenconjunto_machine_learning = frozenset(conjunto_machine_learning)


## Conjunto de texto
meu_texto = "Bem vindo meu nome é Pablo eu gosto muito de nomes e tenho o meu cachorro e gosto muito de cachorro"
conjunto_texto = set(meu_texto.split()) # todas as palavras do texto sem duplicidade
print(conjunto_texto)







