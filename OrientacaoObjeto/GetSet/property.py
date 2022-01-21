
class Guitarra :
    def __init__(self , marca , preco) :
        self._marca = marca
        self._preco = preco
    # def qual_guitarra(self) :
    #     print(f"A guitarra é uma {self._marca}  de _preco : R${self._preco}")

    @property
    def _preco(self) :
        print("Estou passando no @property")
        print(self._preco)
    @property
    def _marca(self) :
        print("Estou passando no @property")
        print(self._marca)
guitarra = Guitarra("Tagima 735" , 1500.00)
