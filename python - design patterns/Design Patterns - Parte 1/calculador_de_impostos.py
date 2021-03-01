from impostos import ISS, ICMS, ICPP, IKCV


class CalculadorDeImpostos(object):

    def realiza_calculo(self, orcamento, imposto):
        ## Design Patter Strategy - passando as funcoes de calculo de imposto como parametro para o método
        imposto_calculado = imposto.calcula(orcamento)

        print("R$", "{0:.2f}".format(imposto_calculado))



if __name__ == '__main__':
    from orcamento import Orcamento, Item

    calculador = CalculadorDeImpostos()

    orcamento = Orcamento()
    orcamento.adiciona_item(Item('Item - 1', 100))
    orcamento.adiciona_item(Item('Item - 2', 50))
    orcamento.adiciona_item(Item('Item - 3', 400))


    print(f'ISS:')
    calculador.realiza_calculo(orcamento, ISS())
    print(f'ICMS:')
    calculador.realiza_calculo(orcamento, ICMS())
    print(f'ICPP:')
    calculador.realiza_calculo(orcamento, ICPP())
    print(f'IKCV:')
    calculador.realiza_calculo(orcamento, IKCV())
