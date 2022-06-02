#programa para criação de planilha de treino

class Personal:
    
  def __init__(self, nome, sobrenome) :
    self.nome = nome
    self.sobrenome = sobrenome
    self.superior = []
    self.inferior = []

  
  def personal(self):
    
    nome_completo = self.nome+" "+self.sobrenome
    print(f"Bem vindo {nome_completo.title()} ")
    print("Vamos montar o treino do aluno!")
    
    self.quantidade= int(input("Quantos exericios : ").strip())
    print("-"*30)

  
  def treino(self):
    
    print("Treino Superior :")
    
    for c in range(1, self.quantidade + 1):
      MontarSuperior = input(f"{c} Exercício de Superior do aluno : ").lower().strip()
      print("-"*30)
      self.superior.append(MontarSuperior)
    
    print("Treino Inferior :")
    
    for i in range(1,self.quantidade + 1):
      MontarInferior = input(f"{i} Exercício de Inferior do aluno : ").lower().strip()
      print("-"*30)
      self.inferior.append(MontarInferior)

  
  def mostrar_treino(self):
    
    question = input("Exibir Treino? [Sim/Não]: ").lower().strip()
    if question == 'sim':
      
      print("-\n"*30)
      print("Superior:\n")
      for treinosuperior in self.superior:
        print(treinosuperior)

      print("-\n"*30)
      print("Inferior:\n")
      for treinoinferior in self.inferior:
        print(treinoinferior)
      print("-"*30)
    
    arquivo = 'treino.txt'
      
    for item in self.superior:
      a = item
      
    for item in self.inferior:
      b = item
      
    try:
      with open(arquivo, 'a') as arq:
        itens = a+"\n"+b
        arq.write(itens)
    except FileNotFoundError:
      return None

class Aluno:
  
  def __init__(self, name, age):
    
    self.name = name
    self.age = age

  def treino_do_aluno(self):
    
    print(f'Aluno: {self.name.title()}')
    print(f'Idade: {self.age}')