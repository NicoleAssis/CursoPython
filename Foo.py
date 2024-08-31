class Foo:
    def __init__(self):
        self.public = 'Isso é publico'
        ...
        
    def metodo_publico(self):
        return 'metodo_public'
    
    
f = Foo()
print(f.public)
print(f.metodo_publico())