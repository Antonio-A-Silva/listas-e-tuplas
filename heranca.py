import numpy as np
from abc import ABCMeta, abstractmethod
from operator import attrgetter
from functools import total_ordering

class Conta(metaclass=ABCMeta):

    def __init__(self, codigo):
        self._codigo = codigo
        self._saldo = 0

    def __eq__(self, other):
        if type(other) != Conta:
            return False
        return sel._codigo == other._codigo and self._saldo == other._saldo

    def __lt__(self, other):
        if self._saldo != other._saldo:
            return self._saldo < other._saldo
        return self._codigo < other._codigo

    def deposita(self, valor):
        self._saldo += valor

    @abstractmethod
    def passa_o_mes(self):
        pass

    def __str__(self):
        return "[>>Codigo {} Saldo {}<<]".format(self._codigo, self._saldo)

class ContaCorrente(Conta):

    def passa_o_mes(self):
        self._saldo -= 2

class ContaPoupanca(Conta):

    def passa_o_mes(self):
        self._saldo *= 1.01
        self._saldo -= 2

class ContaInvestimento(Conta):
    pass

conta16 = ContaCorrente(16)
conta16.deposita(1000)
conta25 = ContaCorrente(25)
conta25.deposita(1000)
conta17 = ContaPoupanca(17)
conta17.deposita(1000)
conta33 = ContaPoupanca(33)
conta33.deposita(1000)

contas = [conta16, conta17, conta25, conta33]
# for conta in contas:
#     conta.passa_o_mes()
#     print(conta)

#conta5 = ContaInvestimento(5)

def extrai_saldo(conta):
    return conta._saldo

print(list(enumerate(contas)))
for conta in sorted(contas, reverse=True):
    print(conta)

for conta in sorted(contas, key=attrgetter("_saldo")):
    print(conta)

for conta in sorted(contas):
    print(conta)

print(conta17 < conta33)