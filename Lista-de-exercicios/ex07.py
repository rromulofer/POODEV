#  Prof. João Luiz de Almeida Filho
#  Disciplina : Paradigma Orientado a Objetos para Desenvolvimento de Software
#  UENF-CCT-LCMAT-CC
#  Data: Setembro 2024
#  Aluno: Rômulo Souza Fernandes

# 7. Composição
# Crie uma classe `Motor` e uma classe `Carro`. A classe `Carro` deve ter um atributo do tipo `Motor`
# e métodos para interagir com o motor.

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
