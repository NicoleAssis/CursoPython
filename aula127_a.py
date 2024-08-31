import json

CAMINHO_ARQUIVO = 'aula127.json'


class Pessoa:
    def __init__(self,nome,idade):
        self.nome = nome
        self.idade = idade
        
        
p1 = Pessoa('João',33)
p2 = Pessoa('Helena',21)
p3 = Pessoa('Joana',11)

bd = [vars(p1 )]

bd = [p1,p2,p3]

with open(CAMINHO_ARQUIVO,'w') as arquivo:
    json.dump(bd,arquivo, ensure_ascii= False, indent = 2)