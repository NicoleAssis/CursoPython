class Pessoa:
    
    def __init__(self,nome,sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome
        
    def falar_nome_classe(self):
        print('Classe Pessoa')
        print(self.nome, self.sobrenome, self.__class__.__name__)
        
    
class Cliente(Pessoa):
    def falar_nome_classe(self):
        print('Classe cli')
        print(self.nome, self.sobrenome, self.__class__.__name__)
    
class Aluno(Pessoa):
    ...
    
c1 = Cliente('Luiz','Otávio')
c1.falar_nome_classe()
a1 = Aluno('Maria','Nicole')
a1.falar_nome_classe()