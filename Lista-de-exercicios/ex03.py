#  Prof. João Luiz de Almeida Filho
#  Disciplina : Paradigma Orientado a Objetos para Desenvolvimento de Software
#  UENF-CCT-LCMAT-CC
#  Data: Setembro 2024
#  Aluno: Rômulo Souza Fernandes

# 3. Construtores
# Implemente uma classe `Produto` que possui um construtor que aceita nome, preço e quantidade
# em estoque. Crie instâncias de `Produto` usando diferentes valores.


class Produto:
    def __init__(self, nome, preco, estoque):
        self.nome = nome
        self.preco = preco
        self.estoque = estoque

    def informacoes(self):
        print(f"Nome: {self.nome}, Preço: {
              self.preco}, Estoque: {self.estoque}")


produto1 = Produto("Camisa", 80.00, 50)
produto2 = Produto("Calça", 120.00, 30)
produto3 = Produto("Tênis", 250.00, 20)

produto1.informacoes()
produto2.informacoes()
produto3.informacoes()
