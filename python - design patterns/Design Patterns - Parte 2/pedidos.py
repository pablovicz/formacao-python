# Design Pattern COMMAND - para fi9la de dados a serem processados e tem uma conexao forte entre
# a operacao a ser relizada sobre esses dados, usamos o dp command


# -*- coding: utf-8 -*-

from datetime import date


class Pedido(object):

    def __init__(self, cliente, valor):
        self.__cliente = cliente
        self.__valor = valor
        self.__status = 'NOVO'
        self.__data_finalizacao = None

    def __str__(self):
        return (f'Cliente: {self.__cliente} \n'
               f'Status: {self.__status} \n'
               f'Data de Finalização:: {self.__data_finalizacao}')

    def paga(self):
        self.__status = 'PAGO'

    def finaliza(self):
        self.__data_finalizacao = date.today()
        self.__status = 'ENTREGUE'

    @property
    def cliente(self):
        return self.__cliente

    @property
    def valor(self):
        return self.__valor

    @property
    def status(self):
        return self.__status

    @property
    def data_finalizacao(self):
        return self.__data_finalizacao


class FilaDeTrabalho(object):

    def __init__(self):
        self.__comandos = []

    def adiciona(self, comando):
        self.__comandos.append(comando)

    def processa(self):
        for comando in self.__comandos:
            comando.executa()


from abc import ABCMeta, abstractmethod


class Comando(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def executa(self):
        pass


class ConcluiPedido(Comando):

    def __init__(self, pedido):
        self.__pedido = pedido

    def executa(self):
        self.__pedido.finaliza()


class PagaPedido(Comando):

    def __init__(self, pedido):
        self.__pedido = pedido

    def executa(self):
        self.__pedido.paga()


if __name__ == '__main__':
    pedido1 = Pedido('Flávio', 150)
    pedido2 = Pedido('Almeida', 250)

    fila_de_trabalho = FilaDeTrabalho()
    fila_de_trabalho.adiciona(PagaPedido(pedido1))
    fila_de_trabalho.adiciona(PagaPedido(pedido2))
    fila_de_trabalho.adiciona(ConcluiPedido(pedido1))

    fila_de_trabalho.processa()

    print(pedido1)
    print(pedido2)
