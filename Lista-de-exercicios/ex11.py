#  Prof. João Luiz de Almeida Filho
#  Disciplina : Paradigma Orientado a Objetos para Desenvolvimento de Software
#  UENF-CCT-LCMAT-CC
#  Data: Setembro 2024
#  Aluno: Rômulo Souza Fernandes

# 11. Métodos Estáticos
# Crie uma classe `MatematicaUtil` com métodos estáticos para calcular o quadrado, cubo e raiz
# quadrada de um número.

import math

class MatematicaUtil:
    @staticmethod
    def quadrado(numero):
        return numero ** 2

    @staticmethod
    def cubo(numero):
        return numero ** 3

    @staticmethod
    def raiz_quadrada(numero):
        return math.sqrt(numero)


print(MatematicaUtil.quadrado(4))
print(MatematicaUtil.cubo(3))
print(MatematicaUtil.raiz_quadrada(16))
