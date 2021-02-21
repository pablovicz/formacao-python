import re
## documentation
### https://docs.python.org/3/library/re.html

email1 =  "Meu numero é 1234-1234"
email2 = "Fale comigo em 12341234"
email3 = "1234-1234 é o meu celular"
email4 = "lalalalal 989762345 lalalala 2144-2432"

## qualquer digito de 1 a 9
padrao = "[0-9]{4,5}[-]*[0-9]{4}"


retorno = re.search(padrao, email1)
print(retorno.group())

retorno = re.search(padrao, email2)
print(retorno.group())

retorno = re.search(padrao, email3)
print(retorno.group())

retorno = re.findall(padrao, email4)
print(retorno)


