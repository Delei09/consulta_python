from produto import Produtos
from carrinho import Carrinho

carrinho = Carrinho()
tenis = Produtos("tenis" , 500)
caneca = Produtos("Caneca" , 15)
short = Produtos("Short" , 30)

carrinho.inserir_produtos(tenis)
carrinho.inserir_produtos(caneca)
carrinho.inserir_produtos(short)
carrinho.listar_produtos()
carrinho.valor_total()