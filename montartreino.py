#program to create a trainning plan
import sys

arquivo = "treino.txt"


class Personal():
    """constroi o perfil do personal trainer"""
    
    def __init__(self, nome, sobrenome):
        """inicializa a classe"""

        self.nome = nome
        self.sobrenome = sobrenome
        self.superior = []
        self.inferior = []

    def personal(self):
        """sauda o usuario e inicia a criação da planilha de treino"""

        nome_completo = self.nome + " " + self.sobrenome
        print("\n" + f"Bem vindo {nome_completo.title()} ")
        print("Vamos montar o treino do aluno!")

        self.quantidade = int(input("Quantos exercicios : ").strip())
        print("-" * 30)

    def treino(self):
        """cria a planilha de treino"""

        print("Treino Superior :")

        for c in range(1, self.quantidade + 1):
            montar_superior = input(
                f"{c} Exercício de Superior do aluno : ").lower().strip()
            print("-" * 30)
            self.superior.append(montar_superior)

        print("Treino Inferior :")

        for i in range(1, self.quantidade + 1):
            montar_inferior = input(
                f"{i} Exercício de Inferior do aluno : ").lower().strip()
            print("-" * 30)
            self.inferior.append(montar_inferior)

    def mostrar_treino(self):
        """mostra a planilha de treino"""

        question = input("Exibir Treino? [Sim/Não]: \n").lower().strip()
        if question == 'sim':

            sys.stdout = open(arquivo, "a")
            print("-" * 30 + "\nSuperior:\n")
            for treino_superior in self.superior:
                print(treino_superior)

            print("-" * 30 + "\nInferior:\n")
            for treino_inferior in self.inferior:
                print(treino_inferior)
            print("-" * 30)


class Aluno():
    """cria perfil do aluno"""
    def __init__(self, nome, *idade):
        """initialize the class"""

        self.nome = nome
        self.idade = idade

    def treino_do_aluno(self):
        """monta o perfil para exibir na planilha"""

        sys.stdout = open(arquivo, "a")
        print("\n" + f'Aluno: {self.nome.title()}')
        print(f'Idade: {self.idade}')
