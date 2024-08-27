#  Prof. João Luiz de Almeida Filho
#  Disciplina : Paradigma Orientado a Objetos para Desenvolvimento de Software
#  UENF-CCT-LCMAT-CC
#  Data: Setembro 2024
#  Aluno: Rômulo Souza Fernandes

# 13. Tratamento de Exceções
# Crie uma classe `Divisao` que tenha um método para dividir dois números inteiros. Lance uma
# exceção personalizada caso ocorra divisão por zero.

class DivisaoPorZeroErro(Exception):
    def __init__(self, mensagem="Divisão por zero não é permitida."):
        self.mensagem = mensagem
        super().__init__(self.mensagem)


class Divisao:
    @staticmethod
    def dividir(numerador, denominador):
        if denominador == 0:
            raise DivisaoPorZeroErro()
        return numerador / denominador


try:
    resultado = Divisao.dividir(6, 3)
    print(f"Resultado: {resultado}")

    resultado = Divisao.dividir(6, 0)
    print(f"Resultado: {resultado}")
except DivisaoPorZeroErro as e:
    print(f"Erro: {e}")
