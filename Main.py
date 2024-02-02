class Main:
    pass

print("\nConta Bancária\n")

from Cliente import Cliente

from Conta import Conta

c1=Cliente("José","9441-8922")
cont=Conta(c1.nome,1893,100)

print("Nome:",cont.titular,"\nNumero:",cont.numero,"\nSeu Saldo:",cont.saldo)