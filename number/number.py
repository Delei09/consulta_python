
import math
from random import randrange


inteiro = 1 # init
flutuante = 2.8 # float
complexo = 2j # complex

# NUMERO RANDOMICO
numeroAleatorio = randrange(1 , 10)
print(numeroAleatorio) # aleatorio 
# MENOR NUMERO
arr = [ 2, 52.6 , -2 , 0 , -32.4]
print( min(arr) ) # -32.4
# MAIOR NUMERO
print( max(arr) ) # 52.6
# NUMERO ELEVADO
tres_ao_cubo = pow( 3, 3) # 27
print(tres_ao_cubo)
### MODULO MATH
# ARRENDONDAR PRA CIMA OU PRA BAIXO
print( math.ceil(flutuante) ) # 3
print( math.floor(flutuante) ) # 2
#ARRENDONDAR DO JEITO QUE PRECISA
valor = round(4.3213 , 2)
print( valor ) # 4,32
valor = round( 4.321321321)
print( valor ) # 4
