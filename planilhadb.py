#planilha de teste.

from montartreino import Personal, Aluno
from bdalunos import ClientesDb

treino = True

professores = {}
alunos = ClientesDb()

while treino:
    prof = input("\nInsira seu nome: ").split()

    for i in prof:
        professores[prof[0]] = prof[1]

    for key, value in professores.items():
        prof = Personal(key, value)
        prof.personal()
        prof.treino()

    aluno = input("\nInsira o Nome do Aluno: ").title()
      
    if aluno in alunos.novo_cadastro(aluno):
      nome = Aluno(aluno)
      nome.treino_do_aluno()
      prof.mostrar_treino()
      treino = False
      
    else:
      print('Aluno nao Cadastrado')
      
      msg = input('\nGostaria de adicionar um novo aluno?(S/N): ')
      if msg == 's':
        alunos.inserir_dados()

      else:
        print('Saindo...')
    
    treino = False