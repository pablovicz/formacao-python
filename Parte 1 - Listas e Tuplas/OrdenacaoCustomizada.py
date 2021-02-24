class ContaSalario:
    def __init__(self, codigo):
        self._codigo = codigo
        self._saldo= 0

    def __eq__(self, outro):
        return self._codigo == outro._codigo

    def deposita(self, valor):
        self._saldo += valor

    def __str__(self):
        return f'[>>Codigo {self._codigo} | Saldo {self._saldo} <<]'

    def __lt__(self, other):  #comparador   ls = LesThan
        return self._saldo < other._saldo

conta1 = ContaSalario(1)
conta1.deposita(1200)

conta2 = ContaSalario(40)
conta2.deposita(250)

conta3 = ContaSalario(13)
conta3.deposita(3000)

contas = [conta1, conta2, conta3]
from operator import attrgetter

##for conta in sorted(contas, key=attrgetter("_saldo")):  ##nao é a melhor situacao, porque estaria expondo um atributo  protegido
##    print(conta)

print(conta1 < conta2)

for conta  in sorted(contas):
    print(conta)

