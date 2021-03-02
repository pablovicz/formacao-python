from abc import ABCMeta, abstractmethod
## Design Pattern STATE
class OrcamentoState(object):
    
    __metaclass__ = ABCMeta

    @abstractmethod
    def aplica_desconto_extra(self, orcamento):
        pass

    @abstractmethod
    def aprova(self, orcamento):
        pass

    @abstractmethod
    def reprova(self, orcamento):
        pass

    @abstractmethod
    def finaliza(self, orcamento):
        pass


class EmAprovacao(OrcamentoState):
    def aplica_desconto_extra(self, orcamento):
        orcamento.adiciona_desconto_extra(orcamento.valor * 0.02)

    def aprova(self, orcamento):
        orcamento.estado_atual = Aprovado()

    def reprova(self, orcamento):
        orcamento.estado_atual = Reprovado()

    def finaliza(self, orcamento):
        raise Exception('Orçamento em aprovação não podem ir para finalizado')

class Aprovado(OrcamentoState):
    def aplica_desconto_extra(self, orcamento):
        orcamento.adiciona_desconto_extra(orcamento.valor * 0.05)

    def aprova(self, orcamento):
        raise Exception('Orçamento já foi aprovado')

    def reprova(self, orcamento):
        raise Exception('Orçamentos aprovados não podem ser reprovados')

    def finaliza(self, orcamento):
        orcamento.estado_atual = Finalizado()


class Reprovado(OrcamentoState):
    def aplica_desconto_extra(self, orcamento):
        raise Exception('Orçamentos reprovados não recebem desconto extra')

    def aprova(self, orcamento):
        raise Exception('Orçamentos reprovados não podem ser aprovados')

    def reprova(self, orcamento):
        raise Exception('Orçamento não pode ser reprovado novamente')

    def finaliza(self, orcamento):
        orcamento.estado_atual = Finalizado()


class Finalizado(OrcamentoState):
    def aplica_desconto_extra(self, orcamento):
        raise Exception('Orçamentos finalizados não recebem desconto extra')

    def aprova(self, orcamento):
        raise Exception('Orçamentos finalizados não podem se aprovados novamente')

    def reprova(self, orcamento):
        raise Exception('Orçamentos finalizados não podem ser reprovados')

    def finalizado(self, orcamento):
        raise Exception('Orçamentos finalizados não podem ser finalizados novamente')

class Orcamento(object):


    def __init__(self):

        self.__itens = []
        self.estado_atual = EmAprovacao()
        self.__desconto_extra = 0

    def aplica_desconto_extra(self):
        self.estado_atual.aplica_desconto_extra(self)

    def adiciona_desconto_extra(self, desconto):
        self.__desconto_extra += desconto

    def aprova(self):
        self.estado_atual.aprova(orcamento)

    def reprova(self):
        self.estado_atual.reprova(orcamento)

    def finaliza(self):
        self.estado_atual.finaliza(orcamento)


    @property
    def valor(self):
        total = 0.0
        for item in self.__itens:
            total += item.valor
        return total - self.__desconto_extra


    def obter_itens(self):
        return tuple(self.__itens)

    @property
    def total_itens(self):
        return len(self.__itens)

    def adiciona_item(self, item):
        self.__itens.append(item)

class Item(object):

    def __init__(self, nome, valor):
        self.__nome = nome
        self.__valor = valor

    @property
    def valor(self):
        return self.__valor

    @property
    def nome(self):
        return self.__nome


if __name__ == '__main__':

    orcamento = Orcamento()
    orcamento.adiciona_item(Item('Item - 1', 100))
    orcamento.adiciona_item(Item('Item - 2', 50))
    orcamento.adiciona_item(Item('Item - 3', 400))

    print(orcamento.valor)
    orcamento.aprova()
    orcamento.aplica_desconto_extra()
    print(orcamento.valor)
    orcamento.finaliza()
    print(orcamento.valor)

