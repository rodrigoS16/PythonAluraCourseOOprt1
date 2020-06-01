class Conta:

    def __init__(self, conta_id, conta_nome, saldo, limite):  # equivale ao construct ou new do ax e c#
        # print("Construindo objeto...{}".format(self))
        # __ = private no c# ou ax, tornando o atributo privado
        self.__numero = conta_id
        from cliente import Cliente
        self.__cliente = Cliente(conta_nome)
        self.__saldo = saldo
        self.__limite = limite

    @property
    def limite(self):
        return self.__limite

    @limite.setter
    def limite(self, limite):
        self.__limite = limite

    @property
    def titular(self):
        return self.__cliente.nome

    @property
    def numero(self):
        return self.__numero

    @property
    def saldo(self):
        return self.__saldo

    def extrato(self):
        # para trabalhar com decimais é da forma abaixo
        # importando a biblioteca
        from decimal import Decimal
        print("Id: {} - Name: {} - Saldo: R$ {:.2f} - Limite: R$ {:.2f}".format(self.__numero
                                                                                , self.__cliente.nome
                                                                                # utilizando a biblioteca de decimais
                                                                                , Decimal(self.__saldo)
                                                                                , self.__limite))

    def deposita(self, valor):
        self.__saldo += valor

    def saque(self, valor):
        if ( self.__can_saque(valor)):
            self.__saldo -= valor
        else:
            print("O valor {:.2f} passou o limite".format(valor))

    def __can_saque(self, valor_a_sacar):
        valor_disponivel_saque = self.__saldo + self.__limite
        return valor_a_sacar <=  valor_disponivel_saque

    def transferencia(self, contaDestino, valor):
        if (self.__can_saque(valor)):
            self.saque(valor)
            contaDestino.deposita(valor)
        else:
            print("O valor {:.2f} passou o limite".format(valor))

    @staticmethod
    def codigo_banco():
        return "001"

    @staticmethod
    def codigos_bancos():
        return {"BB": "001", 'Caixa': '104', 'Bradesco': '237'}

    # def get_saldo(self):    # definição de metodo get
    #    return self.__saldo

    # def set_limite(self, valor):  # definição de metodo set
    #    self.__limite = valor
