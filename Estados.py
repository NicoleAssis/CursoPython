class Camera: 
    def __init__(self, nome, filmando = False):
        self.nome = nome
        self.filmando = filmando
        
        
    def filmar(self):
        if self.filmando:
            print(f'{self.nome} já está filmando...')
            return
        print(f'{self.nome} está filmando...')
        self.filmando = True
    
    def para_filmar(self):
        if not  self.filmando:
            print(f'{self.nome} não está filmando...')
            return
        print(f'{self.nome} está parando de filmar...')
        self.filmando = True
     
    def  fotografar(self):
        if self.filmando:
            print(f'{self.nome} não pode fotogramar filmando')
            return
        print(f'{self.nome}está fotografando')
        
c1 = Camera('Canon')
c2 = Camera('Sony')

c1.filmar()
c1.filmar()
c1.fotografar()
c1.para_filmar()
print(c1.filmando)
print(c2.filmando)