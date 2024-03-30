class Conta:
    def __init__(self, titular, numero, saldo):
        self.saldo = 0
        self.numero = numero
        self.titular = titular

        @property
        def saldo(self):
            return self._saldo

        @saldo.setter
        def get_saldo(self, saldo):
            if (saldo < 0):
                print("Saldo deve ser positivo")
            else:
                self._saldo = saldo

    def saque(self, valor):
        if (self.saldo >= valor):
            self.saldo -= valor
            print("Saque realizado com sucesso")
        else:
            print("Saldo insuficiente")

    def deposita(self, valor):
        self.saldo += valor

    def extrato(self):
        print(Cliente: ", self._titular, " Saldo atual: ", self._saldo)")