
nome = "Vanderlei"
frase = "Hoje é sexta feira"

# PEGAR UM CARACTERE
print( nome[1] ) # a
# PEGAR O TAMANHO DA STRING
print( len(nome) ) # 9
# VER SE CONTEM NA FRASE
print( "sexta"  in frase ) # true
print( "quinta" in frase) # false
# NAO PODE CONTER NA FRASE
print( "script" not in frase) # true
print( "sexta" not in frase) # false
# CONTAR UM PEDAÇO DA STRING
print( frase[0:5]) # Hoje
print( frase[-5: ] ) # feira
print( frase[5:]) # é sexta feira
#TRANSFORMAR EM LETRA MAIUSCULA E MINUSCULA
print( nome.upper() ) # VANDERLEI
print( nome.lower() ) # vanderlei
# MUDAER SÒ A PRIMEIRA LETRA MAIUSCULA
teste = "teste"
print( teste.capitalize() ) # Teste
# RETIRA O ESPAÇO FINAL QUE SOBRA EM UMA FRASE
espaco = " ola, mundo        "
print( espaco.strip() ) # "ola mundo"
# TROCA DETERMINADA CARACTERE OU PALAVRA
print( frase.replace("sexta" , "quinta")) # Hoje é quinta feira
#RETORNAR UM ARRAY SEPARADO DE DETERMINADA FORMA
print(frase.split("é")) #['Hoje ', ' sexta feira']
print(frase.split(" ")) # ['Hoje', 'é', 'sexta', 'feira']
# RETORNA A QUANTIDADE DE CARACTERE DE UMA STRING
print(nome.count("a")) # 1
print(nome.count("e")) # 2
# RETORNA A POSIÇAO QUE ENCONTRA O CARCTERE
print( nome.find("i") ) #8 
print( nome.find("V")) #0
print(nome.find("x")) # -1
# RETORNA SE EXISTE SÒ LETRAS
print(nome.isalpha()) #true
# RETORNA SE EXISTE SÒ NUMERO
a = "123"
print(a.isnumeric()) # true
# RETORNA SE EXISTE SÒ NUMEROS E LETRAS
a = "vanderlei12"
print(nome.isalnum())
# JUNTA DETERMINADO ELEMENTO A UM ARRAY E JUNTA EM UMA STRING
a = ["vanderlei" , "lemos"]
j = "?".join(a)
print(j)  # vanderlei?lemos

