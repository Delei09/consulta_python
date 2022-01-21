from endereco import Endereco

class Cliente :
    def __init__(self, nome , cidade , estado) :
        self.nome = nome
        self.endereco = Endereco(cidade , estado)
    def nome_cliente(self) :
        resposta = self.endereco.pegar_endereco()
        cidade = resposta["Cidade"]
        estado = resposta["UF"]
        print( f"Eu sou {self.nome}  moro cidade: {cidade} estado : {estado}" )