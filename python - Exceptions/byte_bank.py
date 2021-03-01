from models import ContaCorrente, Cliente

def main():

    import sys

    contas = []
    while True:
        try:
            nome = input("Nome do cliente: \n")
            agencia = int(input("Numero de agencia: \n"))
            numero = int(input("Numero da conta corrente: \n"))
            cliente = Cliente(nome, None, None)
            conta_corrente = ContaCorrente(cliente, agencia, numero)
            contas.append(conta_corrente)
        except KeyboardInterrupt:
            print(f'\n\n{len(contas)}(s) contas criadas')
            sys.exit()

if __name__ == '__main__':
    main()
