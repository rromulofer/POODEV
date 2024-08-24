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
