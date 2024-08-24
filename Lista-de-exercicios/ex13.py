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
