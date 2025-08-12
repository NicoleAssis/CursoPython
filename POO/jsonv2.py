import json
import os

# Caminho completo incluindo o nome do arquivo
CAMINHO_PASTA = r'C:\Users\Aluno\Documents\Python\POO'
CAMINHO_ARQUIVO = os.path.join(CAMINHO_PASTA, 'pessoas.json')

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        


p1 = Pessoa('João', 33)
p2 = Pessoa('Helena', 21)
p3 = Pessoa('Joana', 11)

bd = [vars(p1), p2.__dict__, vars(p3)]

def fazer_dump():
    with open(CAMINHO_ARQUIVO,'w') as arquivo:
        json.dump(bd,arquivo,ensure_ascii=False,indent=2)