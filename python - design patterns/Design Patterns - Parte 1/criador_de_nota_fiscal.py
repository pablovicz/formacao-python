from nota_fiscal import NotaFiscal
from datetime import date


class BuilderDeNotaFiscal(object):

    def __init__(self):
        self.__razao_social = None
        self.__cnpj = None
        self.__data_de_emissao = None
        self.__detalhes = None
        self.__itens = None

    def com_razao_social(self, razao_social):
        self.__razao_social = razao_social
        return self  # precisa retornar o proprio builder para poder encadear as chandas Builder().com_bla().com_blbla()...

    def com_cnpj(self, cnpj):
        self.__cnpj = cnpj
        return self

    def com_data_de_emissao(self, data_de_emissao):
        self.__data_de_emissao = data_de_emissao
        return self

    def com_itens(self, itens):
        self.__itens = itens
        return self

    def com_detalhes(self, detalhes):
        self.__detalhes = detalhes
        return self

    def build(self):
        if self.__razao_social is None:
            raise Exception("Razão social deve ser preenchida")
        if self.__cnpj is None:
            raise Exception("CNPJ deve ser preenchida")
        if self.__itens is None:
            raise Exception("Itens devem ser preenchidos")
        if self.__data_de_emissao is None:
            self.__data_de_emissao = date.today()
        if self.__detalhes is None:
            self.__detalhes = ''

        return NotaFiscal(razao_social=self.__razao_social, cnpj=self.__cnpj,
                          itens=self.__itens, data_de_emissao=self.__data_de_emissao,
                          detalhes=self.__detalhes)