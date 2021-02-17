
def cria_conta(numero, titular, saldo, limite):
    conta = {"numero": numero, "titular": titular, "saldo": saldo, "limite": limite}

    return conta

def deposita(conta, valor):
    conta["saldo"] += valor

def saca(conta, valor):
    conta["saldo"] -= valor

def extrato(conta):
    print("Saldo: {}".format(conta["saldo"]))



conta = cria_conta(123, "Pablo", 100.0, 1000.)
extrato(conta)
deposita(conta, 50)
extrato(conta)
saca(conta, 20)
extrato(conta)


from conta import Conta
conta2 = Conta(456, "Kaoana", 200.00, 2000.0)


conta2.extrato()

conta2.deposita(100.00)

conta2.extrato()

conta2.saca(10.00)

conta2.extrato()


print(conta2.saldo)
print(conta2.titular)
print(conta2.limite)

conta2.saca(5000)




