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
