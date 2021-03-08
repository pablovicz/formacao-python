from unittest import TestCase

from src.leilao.dominio import Usuario, Lance, Leilao, Avaliador


class TestAvaliador(TestCase):

    # chama antes de cada teste -> CriaCenario dos testes
    def setUp(self):
        self.gui = Usuario('Gui')
        self.lance_do_gui = Lance(self.gui, 100.0)
        self.leilao = Leilao('Celular')

    # padrao de nome: o que deve retornar e depois situacao
    # também poderia ser:
    # test_deve_quando_adicionados_em_ordem_crescente_retornar_o_maior_e_o_menor_valor_de_um_lance
    ## situacao primeiro e depois o retorno esperado
    def test_deve_retornar_o_maior_e_o_menor_valor_de_um_lance_quando_adicionados_em_ordem_crescente(self):
        yuri = Usuario('Yuri')
        lance_do_yuri = Lance(yuri, 150.0)

        self.leilao.lances.append(self.lance_do_gui)
        self.leilao.lances.append(lance_do_yuri)

        avaliador = Avaliador()
        avaliador.avalia(self.leilao)

        menor_valor_esperado = 100.0
        maior_valor_esperado = 150.0

        self.assertEqual(menor_valor_esperado, avaliador.menor_lance)
        self.assertEqual(maior_valor_esperado, avaliador.maior_lance)


    def test_deve_retornar_o_maior_e_o_menor_valor_de_um_lance_quando_adicionados_em_ordem_decrescente(self):
        self.leilao.lances.append(self.lance_do_gui)

        yuri = Usuario('Yuri')
        lance_do_yuri = Lance(yuri, 150.0)
        self.leilao.lances.append(lance_do_yuri)

        avaliador = Avaliador()
        avaliador.avalia(self.leilao)

        menor_valor_esperado = 100.0
        maior_valor_esperado = 150.0

        self.assertEqual(menor_valor_esperado, avaliador.menor_lance)
        self.assertEqual(maior_valor_esperado, avaliador.maior_lance)


    def test_deve_retornar_o_mesmo_valor_para_maior_e_menor_lance_quando_leilao_tiver_um_lance(self):
        self.leilao.lances.append(self.lance_do_gui)

        avaliador = Avaliador()
        avaliador.avalia(self.leilao)

        self.assertEqual(100.0, avaliador.maior_lance)
        self.assertEqual(100.0, avaliador.menor_lance)

    def test_deve_retornar_o_maior_e_o_menor_lance_quando_leilao_tiver_3_lances(self):


        yuri = Usuario('Yuri')
        vini = Usuario('Vini')
        lance_do_yuri = Lance(yuri, 150.0)
        lance_do_vini = Lance(vini, 200.0)
        self.leilao.lances.append(self.lance_do_gui)
        self.leilao.lances.append(lance_do_yuri)
        self.leilao.lances.append(lance_do_vini)


        avaliador = Avaliador()
        avaliador.avalia(self.leilao)

        menor_valor_esperado = 100.0
        maior_valor_esperado = 200.0

        self.assertEqual(menor_valor_esperado, avaliador.menor_lance)
        self.assertEqual(maior_valor_esperado, avaliador.maior_lance)
