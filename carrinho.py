class Carrinho:
    def __init__(self) -> None:
        self._produtos = []
        
        
    def total (self):
        return sum([p.preco for p in  self._produtos])
    
    def list_produtos(self):
        print()
        for  produto in self._produtos:
            print(produto.nome, produto.preco)
        print()
        
    def inserirprodutos(self, *produtos):
            self._produtos.extend(produtos)
        
class Produto:
    def __init__(self,nome, preco) -> None:
        self.nome = nome
        self.preco = preco
        
carrinho = Carrinho()
p1,p2 = Produto('Caneta',1.20), Produto('Camiseta',20)


carrinho.inserirprodutos(p1,p2)
carrinho.list_produtos()
print(carrinho.total())