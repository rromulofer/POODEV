class Veiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo


class Carro(Veiculo):
    def __init__(self, marca, modelo, numero_portas):
        super().__init__(marca, modelo)
        self.numero_portas = numero_portas

    def informacoes(self):
        print(f"Marca: {self.marca}, Modelo: {
              self.modelo}, Número de portas: {self.numero_portas}")

    def ligar(self):
        print(f"O {self.modelo} está ligado.")

    def desligar(self):
        print(f"O {self.modelo} está desligado.")


carro = Carro("Fiat", "Uno", 4)
carro.informacoes()
carro.ligar()
carro.desligar()
