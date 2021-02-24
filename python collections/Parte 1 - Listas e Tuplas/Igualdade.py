import PolimorfismoEArrays

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


conta1 = PolimorfismoEArrays.ContaCorrente(15)
conta2 = ContaSalario(15)

## por padrao o python só retornará que os dois sao iguais se eles estiverem no mesmo lugar na memoria
# se quisermos uma comparacao dos valores definimos o metodo __eq__

print(conta1 == conta2)


print(conta1 in [conta2])
print(conta2 in [conta1])
