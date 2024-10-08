#  Prof. João Luiz de Almeida Filho
#  Disciplina : Paradigma Orientado a Objetos para Desenvolvimento de Software
#  UENF-CCT-LCMAT-CC
#  Data: Setembro 2024
#  Aluno: Rômulo Souza Fernandes

# 14. Coleções (ArrayList ou equivalente)
# Implemente uma classe `Biblioteca` que contém uma lista de objetos `Livro`. Adicione métodos para
# adicionar, remover e listar livros.

class Livro:
    def __init__(self, titulo):
        self.titulo = titulo

    def __str__(self):
        return self.titulo


class Biblioteca:
    def __init__(self):
        self.livros = []

    def adicionar_livro(self, livro):
        self.livros.append(livro)
        print(f"Livro '{livro}' adicionado à biblioteca.\n")

    def remover_livro(self, livro):
        if livro in self.livros:
            self.livros.remove(livro)
            print(f"\nLivro '{livro}' removido da biblioteca.")
        else:
            print(f"Livro '{livro}' não encontrado na biblioteca.\n")

    def listar_livros(self):
        if self.livros:
            print("\nLivros na biblioteca:")
            for livro in self.livros:
                print(f" - {livro}")
        else:
            print("Nenhum livro na biblioteca.\n")


biblioteca = Biblioteca()
livro1 = Livro("Dom Quixote")
livro2 = Livro("O Guarani")

biblioteca.adicionar_livro(livro1)
biblioteca.adicionar_livro(livro2)

biblioteca.listar_livros()

biblioteca.remover_livro(livro1)

biblioteca.listar_livros()
