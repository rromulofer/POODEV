#  Prof. João Luiz de Almeida Filho
#  Disciplina : Paradigma Orientado a Objetos para Desenvolvimento de Software
#  UENF-CCT-LCMAT-CC
#  Data: Setembro 2024
#  Aluno: Rômulo Souza Fernandes

# 19. Desenvolvimento de um Sistema de Gestão de Funcionários
# Desenvolva um sistema básico que permite gerenciar funcionários, incluindo funcionalidades para
# adicionar, remover, atualizar e listar informações dos funcionários. Não utilize banco de dados;
# armazene os dados em memória.

class Funcionario:
    def __init__(self, id_funcionario, nome, cargo, salario):
        self.id_funcionario = id_funcionario
        self.nome = nome
        self.cargo = cargo
        self.salario = salario

    def __str__(self):
        return f"ID: {self.id_funcionario}, Nome: {self.nome}, Cargo: {self.cargo}, Salário: R${self.salario:.2f}"


class Sistema:
    def __init__(self):
        self.funcionarios = []

    def adicionar_funcionario(self, funcionario):
        self.funcionarios.append(funcionario)
        print(f"Funcionário {funcionario.nome} adicionado com sucesso.")

    def remover_funcionario(self, id_funcionario):
        for funcionario in self.funcionarios:
            if funcionario.id_funcionario == id_funcionario:
                self.funcionarios.remove(funcionario)
                print(f"Funcionário {funcionario.nome} removido com sucesso.")
                return
        print(f"Funcionário com ID {id_funcionario} não encontrado.")

    def atualizar_funcionario(self, id_funcionario, nome=None, cargo=None, salario=None):
        for funcionario in self.funcionarios:
            if funcionario.id_funcionario == id_funcionario:
                if nome:
                    funcionario.nome = nome
                if cargo:
                    funcionario.cargo = cargo
                if salario:
                    funcionario.salario = salario
                print(f"Funcionário {funcionario.id_funcionario} atualizado com sucesso.")
                return
        print(f"Funcionário com ID {id_funcionario} não encontrado.")

    def listar_funcionarios(self):
        if not self.funcionarios:
            print("Nenhum funcionário cadastrado.")
        else:
            for funcionario in self.funcionarios:
                print(funcionario)


sistema = Sistema()

funcionario1 = Funcionario(1, "Rômulo", "Desenvolvedor", 5000.00)
funcionario2 = Funcionario(2, "Miguel", "Designer Junior", 4500.00)
funcionario3 = Funcionario(3, "Carol", "Gerente de Projetos", 6000.00)

sistema.adicionar_funcionario(funcionario1)
sistema.adicionar_funcionario(funcionario2)
sistema.adicionar_funcionario(funcionario3)

print("\nLista de funcionários:")
sistema.listar_funcionarios()

print("\nAtualizando funcionário ID 2:")
sistema.atualizar_funcionario(2, nome="Miguel", cargo="Designer Pleno", salario=5000.00)

print("\nLista de funcionários atualizada:")
sistema.listar_funcionarios()

print("\nRemovendo funcionário ID 1:")
sistema.remover_funcionario(1)

print("\nLista de funcionários após remoção:")
sistema.listar_funcionarios()
