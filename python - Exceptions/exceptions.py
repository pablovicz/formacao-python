class OperacaoFinanceiraError(Exception):
    pass

class SaldoInsuficienteError(OperacaoFinanceiraError):
    def __init__(self, message='', saldo=None, valor=None, *args, **kwargs):
        self.saldo = saldo
        self.valor = valor
        msg = 'Saldo insuficiente para efetuar transação \n' \
            f'Saldo atual: {self.saldo} \n Valor a ser sacado: {self.valor}'
        self.msg = message or msg
        super(SaldoInsuficienteError, self).__init__(self.msg, self.valor, self.saldo, *args)

