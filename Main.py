class Main:
    pass

print("\nConta Bancária\n")

from Cliente import Cliente

from Conta import Conta

c1=Cliente("José","9441-8922")
conta=Conta(c1.get_nome(),1892)

conta.deposita(100)
conta.saque(50)
conta.extrato()
