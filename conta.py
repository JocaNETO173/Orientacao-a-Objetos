class Conta:
    def __init__(self, numero, titular, saldo, limite=1000):
        # print("Construindo objetos! {}".format(self))
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        # conta1 = Conta(156, "Sicrano", 0.00, limite=1000)
        # conta2 = Conta(127, "Ciclano", 0.00, limite=1000)
        # conta3 = Conta(890, "Quilhano", 0.00, limite=1000)

    def depositar(self, valorDep):
        if(valorDep < 0):
            print("Não existe número negativo seu burro!")
        else:
            self.__saldo += valorDep

    def sacar(self, valor):
        if self.__saldo < valor:
            print("Não é possível sacar este valor, pois você não tem dinheiro suficiente")
        else:
            self.__saldo -= valor

    def extrato(self):
            print(f"Saldo do titular {self.__titular}: {self.__saldo}")

    def transferir(self, valor, destino):
        self.sacar(valor)
        destino.depositar(valor)