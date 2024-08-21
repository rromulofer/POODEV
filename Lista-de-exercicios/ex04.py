class Calculadora:
    def adicionar(self, a, b):
        return a + b

    def subtrair(self, a, b):
        return a - b

    def multiplicar(self, a, b):
        return a * b

    def dividir(self, a, b):
        try:
            return a / b
        except ZeroDivisionError:
            return "Erro"


calcular = Calculadora()

print(calcular.adicionar(2, 3))
print(calcular.subtrair(7, 8))
print(calcular.multiplicar(5, 3))
print(calcular.dividir(50, 2))
