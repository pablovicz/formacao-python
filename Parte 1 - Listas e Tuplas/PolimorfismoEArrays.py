import pip
from abc import ABCMeta, abstractmethod

class Conta(metaclass=ABCMeta):

    def __init__(self, codigo):
        self._codigo = codigo
        self._saldo = 0

    def deposita(self, valor):
        self._saldo += valor

    def __str__(self):
        return f'[>>Codigo {self._codigo} | Saldo {self._saldo} <<]'

    @abstractmethod
    def passa_o_mes(self):
        pass

class ContaCorrente(Conta):

    def passa_o_mes(self):
        self._saldo -= 2

class ContaPoupanca(Conta):

    def passa_o_mes(self):
        self._saldo *= 1.01
        self._saldo -= 3

class ContaInvenstimento(Conta):
    pass


## conta1 = ContaInvenstimento()   erro! tem que implementar o método passa_o_mes()

conta16 = ContaCorrente(16)
conta16.deposita(1000)
conta16.passa_o_mes()
print(conta16)

conta17 = ContaPoupanca(17)
conta17.deposita(1000)
conta17.passa_o_mes()
print(conta17)


contas = [conta16, conta17]

for conta in contas:
    conta.passa_o_mes() # duck typing
    print(conta)

## Array - evitaremos usar
### Usado para maior performance com numeros
### declara-se o tipo, e depois todos os valores deverao ser do tipo especificado

import array as arr
numeros = arr.array('d', [1 , 3.5])
print("Array", numeros)

## se precisamos de trabalho numérico usamos o numpy

## Numpy
### Preferir sempre no lugar de arrays
### precisa instalar

#!pip install numpy

import numpy as np

numeros = np.array([1, 3.5])
print("numpy", numeros)