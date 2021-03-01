# -*- coding> UTF-8 -*-
from descontos import DescontoPorMaisDeCincoItens, DescontosPorMaisDeQuinhentosReais, SemDesconto

class CalculadorDeDescontos(object):

    def calcula(self, orcamento):
        desconto = DescontoPorMaisDeCincoItens(
            DescontosPorMaisDeQuinhentosReais(
                SemDesconto()
            )
        )

        return desconto.calcula(orcamento)

if __name__ == '__main__':
    from orcamento import Orcamento, Item

    orcamento = Orcamento()

    orcamento.adiciona_item(Item('Item - 1', 100))
    orcamento.adiciona_item(Item('Item - 2', 50))
    orcamento.adiciona_item(Item('Item - 3', 400))

    print(orcamento.valor)

    calculador = CalculadorDeDescontos()

    desconto_calculado = calculador.calcula(orcamento)
    print(f'Desconto calculado {desconto_calculado}')



