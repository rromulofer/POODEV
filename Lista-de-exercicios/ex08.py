#  Prof. João Luiz de Almeida Filho
#  Disciplina : Paradigma Orientado a Objetos para Desenvolvimento de Software
#  UENF-CCT-LCMAT-CC
#  Data: Setembro 2024
#  Aluno: Rômulo Souza Fernandes

# 8. Associação e Agregação
# Implemente uma classe `Escola` que contém uma lista de objetos da classe `Aluno`. A classe
# `Aluno` deve ter atributos como nome, matrícula e nota.

class Aluno:
    def __init__(self, nome, matricula, nota):
        self.nome = nome
        self.matricula = matricula
        self.nota = nota


class Escola:
    def __init__(self):
        self.alunos = []

    def adicionar_aluno(self, aluno):
        self.alunos.append(aluno)

    def listar_alunos(self):
        for aluno in self.alunos:
            print(f"Nome: {aluno.nome}, Matrícula: {
                  aluno.matricula}, Nota: {aluno.nota}")


aluno1 = Aluno("Charlotte", "121", 9.0)
aluno2 = Aluno("Miguellito", "122", 8.5)
aluno3 = Aluno("Alfredo", "123", 5.0)

escola = Escola()
escola.adicionar_aluno(aluno1)
escola.adicionar_aluno(aluno2)
escola.adicionar_aluno(aluno3)

escola.listar_alunos()
