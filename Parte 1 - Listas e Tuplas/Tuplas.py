class ContaCorrente:

    def __init__(self, codigo):
        self.codigo = codigo
        self.saldo = 0

    def deposita(self, valor):
        self.saldo += valor

    def __str__(self):
        return f'[>>Codigo {self.codigo} | Saldo {self.saldo} <<]'

conta_do_gui = ContaCorrente(15)

print(conta_do_gui)


conta_da_dani = ContaCorrente(47865)
conta_da_dani.deposita(1000)

contas = [conta_da_dani, conta_da_dani]
print(contas)