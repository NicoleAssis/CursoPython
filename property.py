class Caneta:
    def __init__(self,cor):
        self._cor = cor
        
        
    def get_cor(self):
        return self._cor   
    
    
    @property
    def cor(self):
        return self._cor
    
    @cor.setter
    def cor(self,valor):
        if valor == "Rosa":
            raise ValueError('Não aceito essa cor')
        self._cor = valor
      
    
    
caneta = Caneta('Azul')
caneta.cor = 'Rosa'

print(caneta.cor)
print(caneta.cor)
