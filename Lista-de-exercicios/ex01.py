class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def informacoes(self):
        print(f"Nome: {self.nome}, Idade: {self.idade} anos")

pessoa1 = Pessoa("Rômulo", 24)
pessoa1.informacoes()
