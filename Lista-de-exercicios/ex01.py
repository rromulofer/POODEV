#  Prof. João Luiz de Almeida Filho
#  Disciplina : Paradigma Orientado a Objetos para Desenvolvimento de Software
#  UENF-CCT-LCMAT-CC
#  Data: Setembro 2024
#  Aluno: Rômulo Souza Fernandes

#  1. Classes e Objetos Básicos
# Implemente uma classe `Pessoa` com atributos para nome, idade e um método para exibir as
# informações da pessoa.

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def informacoes(self):
        print(f"Nome: {self.nome}, Idade: {self.idade} anos")

pessoa1 = Pessoa("Rômulo", 24)
pessoa1.informacoes()
