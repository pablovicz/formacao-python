from unittest import TestCase

from src.leilao.dominio import Usuario, Lance, Leilao


class TestLeilao(TestCase):

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

        self.leilao.propoe(self.lance_do_gui)
        self.leilao.propoe(lance_do_yuri)

        menor_valor_esperado = 100.0
        maior_valor_esperado = 150.0

        self.assertEqual(menor_valor_esperado, self.leilao.menor_lance)
        self.assertEqual(maior_valor_esperado, self.leilao.maior_lance)


    def test_deve_retornar_o_maior_e_o_menor_valor_de_um_lance_quando_adicionados_em_ordem_decrescente(self):
        self.leilao.propoe(self.lance_do_gui)

        yuri = Usuario('Yuri')
        lance_do_yuri = Lance(yuri, 150.0)
        self.leilao.propoe(lance_do_yuri)

        menor_valor_esperado = 100.0
        maior_valor_esperado = 150.0

        self.assertEqual(menor_valor_esperado, self.leilao.menor_lance)
        self.assertEqual(maior_valor_esperado, self.leilao.maior_lance)


    def test_deve_retornar_o_mesmo_valor_para_maior_e_menor_lance_quando_leilao_tiver_um_lance(self):
        self.leilao.propoe(self.lance_do_gui)

        self.assertEqual(100.0, self.leilao.maior_lance)
        self.assertEqual(100.0, self.leilao.menor_lance)

    def test_deve_retornar_o_maior_e_o_menor_lance_quando_leilao_tiver_3_lances(self):


        yuri = Usuario('Yuri')
        vini = Usuario('Vini')
        lance_do_yuri = Lance(yuri, 150.0)
        lance_do_vini = Lance(vini, 200.0)
        self.leilao.propoe(self.lance_do_gui)
        self.leilao.propoe(lance_do_yuri)
        self.leilao.propoe(lance_do_vini)

        menor_valor_esperado = 100.0
        maior_valor_esperado = 200.0

        self.assertEqual(menor_valor_esperado, self.leilao.menor_lance)
        self.assertEqual(maior_valor_esperado, self.leilao.maior_lance)

    # se leilao nao tiber lances, deve permitir propor um lance
    def test_deve_permitir_propor_um_lance_caso_o_leilao_nao_tenha_lances(self):
        self.leilao.propoe(self.lance_do_gui)
        quantidade_de_lances_recebida = len(self.leilao.lances)
        self.assertEqual(1, quantidade_de_lances_recebida)

    # se o ultmo usuario for diferente, deve permitir propor o lance
    def test_deve_permitir_propor_um_lance_caso_o_ultimo_usuario_seja_diferente(self):

        with self.assertRaises(ValueError):
            yuri = Usuario('Yuri')
            lance_do_yuri = Lance(yuri, 200.00)
            self.leilao.propoe(lance_do_yuri)
            self.leilao.propoe(self.lance_do_gui)

            quantidade_de_lances_recebido = len(self.leilao.lances)

            self.assertEqual(2, quantidade_de_lances_recebido)


    # se o ultimo usuario for o mesmo, nao deve permitir propor o lance
    def test_nao_deve_permitir_propor_lance_caso_o_usuario_seja_o_mesmo(self):
        lance_de_gui200 = Lance(self.gui, 200.00)

        with self.assertRaises(ValueError):
            self.leilao.propoe(lance_de_gui200)
            self.leilao.propoe(self.lance_do_gui)






