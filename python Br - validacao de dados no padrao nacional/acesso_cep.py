import requests


def cep_eh_valido(cep):
    if len(cep) == 8:
        return True
    else:
        return False


class BuscaEndereco:

    def __init__(self, cep):
        cep = str(cep)
        if cep_eh_valido(cep):
            self.cep = cep
        else:
            raise ValueError("CEP inválido")

    def __str__(self):
        return self.format_cep()

    def format_cep(self):
        return f'{self.cep[:5]}-{self.cep[5:]}'

    def retorna_endereco(self):
        r = requests.get(f'https://viacep.com.br/ws/{self.cep}/json/')
        retorno = r.json()

        if retorno["logradouro"] == "":
            return f'{retorno["localidade"]}-{retorno["uf"]}, CEP {self.format_cep()}'
        else:
            return f'Rua {retorno["logradouro"]}, {retorno["bairro"]}, {retorno["localidade"]}-{retorno["uf"]}, CEP {self.format_cep()}'