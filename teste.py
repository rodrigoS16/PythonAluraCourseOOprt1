def cria_conta(conta_id, conta_nome, saldo, limite):
    conta = {"numero" : conta_id, "titular" : conta_nome, "saldo" : saldo, "limite" : limite }
    return conta


def deposita(conta, valor):
    conta["saldo"] += valor


def saque(conta, valor):
    conta["saldo"] -= valor


def extrato(conta):
    print("Saldo é {:2f}".format(conta["saldo"]))

from conta import Conta
conta = Conta(123, "teste", 55.0, 1000.0)
conta.extrato()
conta2 = Conta(321, "Marco", 100.0, 1000.0)
conta2.extrato()
# conta = cria_conta(123, "x", 10.0, 100.0)
conta.deposita(100.00)
conta.extrato()
conta2.saque(10.00)
conta2.extrato()

conta.transferencia(conta2, 50)
conta.extrato()

# print(conta.get_titular())
print(conta.codigo_banco())
print(conta.codigos_bancos()['Bradesco'])

from cliente import Cliente
cliente = Cliente("joaquim")

print(cliente.nome)
cliente.nome = "anderson"
print(cliente.nome)


#outraRef = conta2
#outraRef.extrato()
#outraRef = None  # equivale ao var = null do c#

#print(outraRef)

#from datas import Data
#data = Data(21, 11, 2007)
#data.formaData()

#Data.default_Data  #atributo estatico