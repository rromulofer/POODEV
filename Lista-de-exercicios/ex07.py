class Motor:
    def __init__(self):
        self.ligado = False

    def ligar(self):
        self.ligado = True

    def desligar(self):
        self.ligado = False


class Carro:
    def __init__(self):
        self.motor = Motor()

    def ligar_motor(self):
        self.motor.ligar()
        print("Motor ligado.")

    def desligar_motor(self):
        self.motor.desligar()
        print("Motor desligado.")

    def estado_do_motor(self):
        if self.motor.ligado:
            estado = "ligado"
        else:
            estado = "desligado"

        print(f"O motor está {estado}.")


meu_carro = Carro()

meu_carro.estado_do_motor()
meu_carro.ligar_motor()
meu_carro.estado_do_motor()
meu_carro.desligar_motor()
meu_carro.estado_do_motor()
