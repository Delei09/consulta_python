
class Produtos :
    def __init__(self , nome , valor) :
        self.nome = nome 
        self.valor = valor
        self.produtos = []
    def get_produto (self) :
        for produto in self.produtos :
            print(f"{self.nome} de valor {self.valor}")

        
        