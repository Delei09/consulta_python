
class Endereco :
    def __init__(self , cidade , estado) :
        self.cidade = cidade
        self.estado = estado

    def pegar_endereco(self) :
        local = {
            "Cidade" : self.cidade ,
            "UF": self.estado
        }
        print(local)
        return local
