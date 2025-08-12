import json
import os

# Caminho completo incluindo o nome do arquivo
CAMINHO_PASTA = r'C:\Users\Aluno\Documents\Python\POO'
CAMINHO_ARQUIVO = os.path.join(CAMINHO_PASTA, 'pessoas.json')

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        
    def to_dict(self):
        return {'nome': self.nome, 'idade': self.idade}

p1 = Pessoa('João', 33)
p2 = Pessoa('Helena', 21)
p3 = Pessoa('Joana', 11)

bd = [p1, p2, p3]

# Converter cada objeto Pessoa em um dicionário
bd_dict = [pessoa.to_dict() for pessoa in bd]

# Criar o diretório se não existir
os.makedirs(CAMINHO_PASTA, exist_ok=True)

with open(CAMINHO_ARQUIVO, 'w', encoding='utf-8') as arquivo:
    json.dump(bd_dict, arquivo, ensure_ascii=False, indent=2)

print(f'Arquivo salvo com sucesso em: {CAMINHO_ARQUIVO}')