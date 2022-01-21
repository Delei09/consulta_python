


class Carrinho :
    def __init__(self) :
        self.produtos = []
    def inserir_produtos (self , produto ) :
        item = {
            "nome" : produto.nome ,
            "valor": produto.valor
        }
        self.produtos.append(item)
    def listar_produtos(self) :
        print(self.produtos)
        # for produto in self.produtos :
        #     print(produto)
    def valor_total (self) :
        valor_total = 0
        for produto in self.produtos :
            print(produto)
            valor_total += produto["valor"]
        print(valor_total)    