#  Prof. João Luiz de Almeida Filho
#  Disciplina : Paradigma Orientado a Objetos para Desenvolvimento de Software
#  UENF-CCT-LCMAT-CC
#  Data: Setembro 2024
#  Aluno: Rômulo Souza Fernandes

# 10. Classes Abstratas
# Implemente uma classe abstrata `FormaGeometrica` com um método abstrato `calcularArea()`. Crie
# subclasses `Quadrado` e `Circulo` que implementam o método `calcularArea()`.

from abc import ABC, abstractmethod
import math


class FormaGeometrica(ABC):
    @abstractmethod
    def calcularArea(self):
        pass


class Quadrado(FormaGeometrica):
    def __init__(self, lado):
        self.lado = lado

    def calcularArea(self):
        return self.lado ** 2


class Circulo(FormaGeometrica):
    def __init__(self, raio):
        self.raio = raio

    def calcularArea(self):
        return math.pi * (self.raio ** 2)


quadrado = Quadrado(5)
circulo = Circulo(2)

print(f"Área do quadrado: {quadrado.calcularArea()}")
print(f"Área do círculo: {circulo.calcularArea():.2f}")
