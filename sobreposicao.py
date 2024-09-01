class MinhaString(str):
    def upper(self):
        print('Chamou Upper')
        #return super().upper()
        retorno = super(MinhaString,self).upper()
        print('Depois do Upper')
        return retorno
        
    
    
string = MinhaString('Luiz')
print(string.upper())