from trabalhador import Trabalhador
from ferramenta import Ferramenta

rolo = Ferramenta("Rolo De Parede")
pintor = Trabalhador("Pintor" , rolo)

pintor.funcao_trabalhador()
pintor.ferramenta.usar_ferramenta()

computador = Ferramenta("Computador")
programador = Trabalhador("Programador" , computador)

programador.funcao_trabalhador()
programador.ferramenta.usar_ferramenta()