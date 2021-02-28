class SaldoInsuficienteError(Exception):
    def __init__(self, message='', saldo=None, valor=None, *args, **kwargs):
        self.saldo = saldo
        self.valor = valor
        msg = 'Saldo insuficiente para efetuar transação \n' \
            f'Saldo atual: {self.saldo} \n Valor a ser sacado: {self.valor}'
        super(SaldoInsuficienteError, self).__init__(message or msg)