class Conta:
    def __init__(self, numero, titular, saldo, limite=100):
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite_especial = limite

    # Declaração dos métodos (funções)

    def depositar(self, valorDep):
        if (valorDep <= 0):
            print("Não existe número negativo seu burro!")
        else:
            self.__saldo += valorDep

    def __saque_permitido(self, valor_saque):
        valor_disponivel_saque = self.__saldo + self.__limite_especial
        return valor_saque <= valor_disponivel_saque

    def sacar(self, valor):
        if (self.__saque_permitido(valor)):
            self.__saldo -= valor

        else:
            print(
                "Não é possível sacar este valor, pois você não tem dinheiro suficiente")

    def extrato(self):
        print(f"Saldo: {self.__saldo}")

    def transferir(self, valor, destino):
        if (self.__saque_permitido(valor)):
            self.sacar(valor)
            destino.depositar(valor)
            
        else:
            print("Saldo Insuficiente")
    # Método para retornar apenas valores das propriedades
    # valores das propriedades

    @property
    def saldo(self):
        return self.__saldo

    @property
    def titular(self):
        return self.__titular

    @property
    def numero(self):
        return self.__numero

    @property
    def limite(self):
        return self.__limite_especial
    
    @staticmethod
    def codigo_banco():
        return '001'
    
    @staticmethod
    def codigos_bancos():
        return {'BB':'001', 'Caixa':'104', 'Nubank':'260'}

    # Redefinindo valor das variáveis
    @limite.setter
    def limite(self, limite):
        self.__limite_especial = limite
