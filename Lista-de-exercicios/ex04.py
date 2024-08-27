#  Prof. João Luiz de Almeida Filho
#  Disciplina : Paradigma Orientado a Objetos para Desenvolvimento de Software
#  UENF-CCT-LCMAT-CC
#  Data: Setembro 2024
#  Aluno: Rômulo Souza Fernandes

# 4. Métodos e Sobrecarga
# Implemente uma classe `Calculadora` com métodos para adicionar, subtrair, multiplicar e dividir.
# Sobrecargue os métodos para operar com diferentes números de parâmetros.

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
