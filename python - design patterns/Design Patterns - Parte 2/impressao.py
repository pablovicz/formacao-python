#Design Pattern Visitor - visitam arvore de elementos e fazem operacoes definidas

class Impressao(object):

    def visita_soma(self, soma):
        print(
            '(',
            soma.expressao_esquerda.aceita(self),
            '+',
            soma.expressao_direita.aceita(self),
            ')'
        )

    def visita_subtracao(self, subtracao):
        print(
            '(',
            subtracao.expressao_esquerda.aceita(self),
            '-',
            subtracao.expressao_direita.aceita(self),
            ')'
        )

    def visita_numero(self, numero):
        print(numero.avalia(),)




