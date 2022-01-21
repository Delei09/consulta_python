# Lista é igual a array js
# tuple é um array que nao pode ser mudado e é separado por ()
# dicionario se assemleha a um objeto no js

lista =  ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# PEGAR ALGO EM UM ARRAY
print(lista[2:]) # ['cherry', 'orange', 'kiwi', 'melon', 'mango']
print(lista[-1]) #"[mango]"
# VER SE EXISTE ALGO EM UM ARRAY
if "banana" in lista :
    print("EXISTE PORQUE CAI NO IF")
#ADD ALGO EM DETERMINADO INDEX
lista[1] = "morango"
print(lista)
# ADD E RETIRA ALGUMAS COISAS
lista[1:2] = ["um" , "dois"] # ['apple', 'um', 'dois', 'cherry', 'orange', 'kiwi', 'melon', 'mango']
print(lista)
lista[1:5] = ["um" , "dois"] # ['apple', 'um', 'dois', 'kiwi', 'melon', 'mango']
print(lista)
# INSERE ALGO EM DETERMINADO INDEX
lista.insert(1 , "TO NO INDICE 1")
print(lista)
# ADD ALGO NO ARRAY
lista.append("Append")
print(lista)
# JUNTAR DOIS ARRAYS
segundaLista = ["ola" , "to" , "na" , "segunda"]
segundaLista.extend(lista)
print(segundaLista) # ['ola', 'to', 'na', 'segunda', 'apple', 'banana', 'cherry', 'orange', 'kiwi', 'melon', 'mango']
#REMOVER UM INTEM DO ARRAY
lista.remove("apple")
print( lista ) # ['banana', 'cherry', 'orange', 'kiwi', 'melon', 'mango']
#REMOVER ITEM ESPECIFICO
lista.pop(2)
print(lista)
# LIMPAR A LISTA
lista.clear()
print(lista)
# ORDENA CRESCENTE E DECRESCENTE
a = [1,2,-21,3,4,5,3123,341,321321]
a.sort()
print(a)
a.sort(reverse = True)
print(a)
# ORDENAR Ao contrario o array
lista.reverse()
print( lista )
# SE O ELEMENTO SE REPETE E QUANTAS VEZES
x = lista.count("mango") 
print(x)