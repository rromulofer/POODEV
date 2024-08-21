class ContaBancaria:
    def __init__(self, saldo=0):
        self.__saldo = saldo

    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
            print(f"Depositado: R$ {valor:.2f}")
        else:
            print("Digite um valor positivo")

    def sacar(self, valor):
        if valor > 0:
            if valor <= self.__saldo:
                self.__saldo -= valor
                print(f"Sacado: R$ {valor:.2f}")
            else:
                print("Saldo insuficiente")
        else:
            print("Digite um valor positivo")

    def consultar_saldo(self):
        print(f"Saldo atual: R$ {self.__saldo:.2f}")


conta = ContaBancaria(8000)
conta.consultar_saldo()
conta.depositar(500)
conta.sacar(50)
conta.consultar_saldo()
