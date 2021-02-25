meu_texto = "Bem vindo meu nome é Pablo eu gosto muito desse nome e tenho o meu cachorro e gosto muito de cachorro"
conjunto_texto = set(meu_texto.split())

# organizacao chave - valor
aparicoes = {
    "Pablo": 1,
    "cachorro": 2,
    "nome": 2,
    "vindo":1
}

print(type(aparicoes)) #Dict - dicionario

print(aparicoes["Pablo"])


aparicoes_com_construtor = dict(Pablo = 1, cachorro = 2, nome = 2, vindo = 1)

print(aparicoes_com_construtor)

## Operacoes

## adicionar elementos
aparicoes["Carlos"] = 1
print(aparicoes)

# alterar elementos
aparicoes["Pablo"] = 5
print(aparicoes)

# remover elementos
del aparicoes["Carlos"]
print(aparicoes)

# verificar se valor pertence

print("cachorro" in aparicoes) #procura dentro das CHAVES

# iterar sobre elementos
for elemento in aparicoes:
    print(elemento)

## iterar sobre as chaves
for elemento in aparicoes.keys():
    print(elemento)

## iterar sobre os valores
for elemento in aparicoes.values():
    print(elemento)

## iterar sobre ambos
for elemento in aparicoes.items():
    print(elemento)

## desenpacoranto
for chave, valor in aparicoes.items():
    print(f'Chave: {chave} | Valor: {valor}')




## contando valores dentro de um texto
meu_texto = meu_texto.lower()
aparicoes = {}
for palavra in meu_texto.split():
    ate_agora = aparicoes.get(palavra, 0)
    aparicoes[palavra] = ate_agora + 1

print(aparicoes)


#usando default dict
from collections import defaultdict

aparicoes = defaultdict(int)
for palavra in meu_texto.split():
    ate_agora = aparicoes[palavra]
    aparicoes[palavra] = ate_agora + 1

print(aparicoes)


# outra maneira

aparicoes = defaultdict(int)
for palavra in meu_texto.split():
      aparicoes[palavra] += 1

print(aparicoes)


# outra maneira
from collections import Counter

aparicoes = Counter(meu_texto.split())  # maneira mais rapida
print(aparicoes)









