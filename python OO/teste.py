
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










