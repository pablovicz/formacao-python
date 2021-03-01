from impostos import ISS, ICMS


class Calculador_de_impostos(object):

    def realiza_calculo(self, orcamento, imposto):
        ## Design Patter Strategy - passando as funcoes de calculo de imposto como parametro para o método
        imposto_calculado = imposto.calcula(orcamento)

        print(imposto_calculado)


if __name__ == '__main__':
    from orcamento import Orcamento

    calculador = Calculador_de_impostos()

    orcamento = Orcamento(500)

    calculador.realiza_calculo(orcamento, ISS())
    calculador.realiza_calculo(orcamento, ICMS())
