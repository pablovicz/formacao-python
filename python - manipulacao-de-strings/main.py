'''
sobre_mim = "Meu nome é Pablo e minha idade é 25"
meu_nome = "Pablo"

pertence = meu_nome in sobre_mim
print(pertence)

sub_string = sobre_mim[25:]
print(sub_string)


url = "https://www.bytebank.com.br/cambio?moedaorigem=real"

## obter apenas o valor da moeda de origem
argumento = "moedaorigem=real"

## forma 1 - find
index = argumento.find("=")
print(index)
sub_string = argumento[index + 1:]
print(sub_string)

## forma 2 - split - bom para strings mais simples com 1 tipo de separado, por exemplo
lista_argumentos = argumento.split("=")
print(lista_argumentos[1])

'''

from ExtratorArgumentosUrl import ExtratorArgumentosUrl

url = "https://bytebank.com/cambio?moedaorigem=real&moedadestino=dolar&valor=700"
argumento = ExtratorArgumentosUrl(url)

print(argumento)
'''
ExtratorArgumentosUrl(None)
ExtratorArgumentosUrl("")
'''

moeda_origem, moeda_destino, valor = argumento.extrai_argumentos()
print(moeda_origem, moeda_destino, valor)


