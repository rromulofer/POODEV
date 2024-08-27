#  Prof. João Luiz de Almeida Filho
#  Disciplina : Paradigma Orientado a Objetos para Desenvolvimento de Software
#  UENF-CCT-LCMAT-CC
#  Data: Setembro 2024
#  Aluno: Rômulo Souza Fernandes

# 9. Herança Múltipla (através de interfaces)
# Implemente interfaces `Movimentavel` e `Desenhavel`. Crie uma classe `Personagem` que
# implementa ambas as interfaces, com métodos para mover e desenhar o personagem.

from abc import ABC, abstractmethod

class Movimentavel(ABC):
    @abstractmethod
    def mover(self, x, y):
        pass

class Desenhavel(ABC):
    @abstractmethod
    def desenhar(self):
        pass

class Personagem(Movimentavel, Desenhavel):
    def __init__(self, nome, posicao_x=0, posicao_y=0):
        self.nome = nome
        self.posicao_x = posicao_x
        self.posicao_y = posicao_y
    
    def mover(self, x, y):
        self.posicao_x += x
        self.posicao_y += y
        print(f"{self.nome} moveu-se para a posição ({self.posicao_x}, {self.posicao_y}).")
    
    def desenhar(self):
        print(f"Desenhando o personagem {self.nome} na posição ({self.posicao_x}, {self.posicao_y}).")


personagem = Personagem("Herói")
personagem.mover(10, 5)
personagem.desenhar()
