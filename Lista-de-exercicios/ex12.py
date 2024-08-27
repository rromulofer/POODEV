#  Prof. João Luiz de Almeida Filho
#  Disciplina : Paradigma Orientado a Objetos para Desenvolvimento de Software
#  UENF-CCT-LCMAT-CC
#  Data: Setembro 2024
#  Aluno: Rômulo Souza Fernandes

# 12. Enums
# Implemente uma enumeração `DiasDaSemana` e utilize-a em uma classe `Agenda` para marcar
# compromissos em diferentes dias.

from enum import Enum

class DiasDaSemana(Enum):
    SEGUNDA = 1
    TERCA = 2
    QUARTA = 3
    QUINTA = 4
    SEXTA = 5
    SABADO = 6
    DOMINGO = 7


class Agenda:
    def __init__(self):
        self.compromissos = {dia: [] for dia in DiasDaSemana}

    def marcar_compromisso(self, dia, compromisso):
        if dia in self.compromissos:
            self.compromissos[dia].append(compromisso)
            print(f"Compromisso '{compromisso}' marcado para {dia.name}. \n")
        else:
            print("Dia inválido.")

    def listar_compromissos(self, dia):
        if dia in self.compromissos:
            compromissos = self.compromissos[dia]
            if compromissos:
                print(f"\nCompromissos para {dia.name}: {
                      ', '.join(compromissos)} ")
            else:
                print(f"\nNão há compromissos para {dia.name}.")
        else:
            print("Dia inválido.")


agenda = Agenda()
agenda.marcar_compromisso(DiasDaSemana.SEGUNDA, "Aula Computação Gráfica")
agenda.marcar_compromisso(DiasDaSemana.QUARTA, "Aula POODEV")
agenda.marcar_compromisso(DiasDaSemana.SEXTA, "Revisar materia da semana")

agenda.listar_compromissos(DiasDaSemana.SEGUNDA)
agenda.listar_compromissos(DiasDaSemana.QUARTA)
agenda.listar_compromissos(DiasDaSemana.QUINTA)
agenda.listar_compromissos(DiasDaSemana.SEXTA)
