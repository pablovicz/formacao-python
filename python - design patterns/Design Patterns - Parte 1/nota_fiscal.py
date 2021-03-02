# -*- coding: UTF-8 -*-
# nota_fiscal.py
from datetime import date

class Item(object):

    def __init__(self, descricao, valor):
        self.__descricao = descricao
        self.__valor = valor

    @property
    def descricao(self):
        return self.__descricao

    @property
    def valor(self):
        return self.__valor

class NotaFiscal(object):

    def __init__(self, razao_social, cnpj, itens, data_de_emissao=date.today(), detalhes='', observadores=[]): ##parametros opcionais vem por ultimo
        self.__razao_social = razao_social
        self.__cnpj = cnpj
        self.__data_de_emissao = data_de_emissao
        if len(detalhes) > 20:
            raise Exception('Detalhes da nota não pode ter mais do que 20 caracteres')
        self.__detalhes = detalhes
        self.__itens = itens

        ##Design Pattern - Observer
        for observador in observadores:
            observador(self)



    @property
    def razao_social(self):
        return self.__razao_social

    @property
    def cnpj(self):
        return self.__cnpj

    @property
    def data_de_emissao(self):
        return self.__data_de_emissao

    @property
    def detalhes(self):
        return self.__detalhes

    # nota_fiscal.py
    # código das classes omitidos

if __name__ == '__main__':
    from criador_de_nota_fiscal import BuilderDeNotaFiscal
    from observadores import imprime, envia_por_email, salva_no_banco

    itens = [
       Item(
            'ITEM A',
            100
       ),
       Item(
            'ITEM B',
            200
       )
    ]

    nota_fiscal = NotaFiscal(
        razao_social='FHSA Limitada',
        cnpj='012345678901234',
        itens=itens,
        observadores=[imprime, envia_por_email, salva_no_banco]
    )

'''
    nota_fiscal_com_builder = (BuilderDeNotaFiscal()
                               .com_razao_social('FHSA Limitada')
                               .com_cnpj('012345678901234')
                               .com_itens(itens)
                               .build())
'''
