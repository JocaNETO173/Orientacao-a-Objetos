from .conta import Conta

conta1 = Conta(123, "Pablo", 2136.32, 6000.00)
conta2 = Conta(321, "Eustácio", 1136.32, 4000.00)



conta1.transferir(50, conta2)
conta1.extrato()
conta2.extrato()
