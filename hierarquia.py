class A(object):
    atributo_a = 'Valor a '
    def __init__(self,atributo) -> None:
        self.atributo = atributo
    
    def metodo(self):
        print('A')
        
class B(A):
    atributo_b = 'Valor b '
    
    def __init__(self,atributo,outra_coisa):
        super().__init__(atributo)
        self.outra_coisa = outra_coisa
        
    def metodo(self):
        
        print('B')

class C(B):
    atributo_c = 'Valor c '
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        print('Heyyy')
        
    def metodo(self):
        #super().metodo()
        #super(B,self).metodo()
        print('C')
        
        
# print(C.mro())        
c = C('Outra','Coisa')
print(c.atributo)
print(c.outra_coisa)

# print(c.atributo_a)
# print(c.atributo_b)
# print(c.atributo_c)

# c.metodo()