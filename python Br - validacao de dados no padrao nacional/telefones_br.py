import re

class TelefonesBr:
    def __init__(self, telefone):
        telefone = str(telefone)
        if self.valida_telefone(telefone):
            self.numero = telefone
        else:
            raise ValueError("Número inválido!")

    def __str__(self):
        return self.formata_telefone()

    def valida_telefone(self, telefone):
        padrao = "([0-9]{2,3})?([0-9]{2})([0-9]{4,5})([0-9]{4})"
        resposta = re.findall(padrao, telefone)
        if resposta:
            return True
        else:
            return False

    def formata_telefone(self):
        padrao = "([0-9]{2,3})?([0-9]{2})([0-9]{4,5})([0-9]{4})"
        resposta = re.search(padrao, self.numero)
        if resposta.group(1) == None:
            return f'+55 ({resposta.group(2)}) {resposta.group(3)}-{resposta.group(4)}'
        else:
            return f'+{resposta.group(1)} ({resposta.group(2)}) {resposta.group(3)}-{resposta.group(4)}'











