class Caixa:
    def __init__(self):
        self.itens = []
    
    def adicionar_item(self, item):
        self.itens.append(item)
        print(f"Item '{item}' adicionado à caixa.")
    
    def remover_item(self):
        if self.itens:
            item = self.itens.pop()
            print(f"Item '{item}' removido da caixa.")
            return item
        else:
            print("A caixa está vazia.")
            return None
    
    def listar_itens(self):
        if self.itens:
            print("Itens na caixa:")
            for item in self.itens:
                print(f" - {item}")
        else:
            print("A caixa está vazia.")


caixa = Caixa()
caixa.adicionar_item("Livro")
caixa.adicionar_item(123)
caixa.adicionar_item([1, 2, 3])

caixa.listar_itens()
caixa.remover_item()
caixa.listar_itens()
