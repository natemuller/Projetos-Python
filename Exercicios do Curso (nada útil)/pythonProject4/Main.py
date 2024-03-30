class Main:
    pass

print("Teste")

from Cliente import Cliente

from Conta import Conta

c1 = Cliente("Natan", "51991235815")
conta = Conta(c1.nome, 6565, 0)

print(c1)
print(c1.nome, " e ", c1.telefone)

print(conta)
print(conta.titular, " Numero: ", conta.numero, " Saldo: ", conta.saldo)

conta.deposita(100)
conta.saque(50)
conta.extrato()