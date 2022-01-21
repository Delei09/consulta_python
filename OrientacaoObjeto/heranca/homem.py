from pessoa import Pessoa

class Homem(Pessoa) :
    def __init__(self , nome , idade , sexo) :
        super().__init__(nome , idade)
        self.sexo = sexo
    def qual_sexo(self) :
        print(self.sexo)