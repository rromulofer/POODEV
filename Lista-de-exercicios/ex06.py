#  Prof. João Luiz de Almeida Filho
#  Disciplina : Paradigma Orientado a Objetos para Desenvolvimento de Software
#  UENF-CCT-LCMAT-CC
#  Data: Setembro 2024
#  Aluno: Rômulo Souza Fernandes

# 6. Polimorfismo
# Implemente uma classe `Animal` com um método `emitirSom()`. Crie subclasses `Cachorro` e
# `Gato` que sobrepõem `emitirSom()` para retornar sons específicos.

class Animal:
    def emitirSom(self):
        return "Animal emitindo som"


class Cachorro(Animal):
    def emitirSom(self):
        return "Latindo"


class Gato(Animal):
    def emitirSom(self):
        return "Miando"

passarinho_coronel = Animal()
cachorro_alfredo = Cachorro()
gato_jubileu = Gato()

print(passarinho_coronel.emitirSom())
print(cachorro_alfredo.emitirSom())
print(gato_jubileu.emitirSom())
