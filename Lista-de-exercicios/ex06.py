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
