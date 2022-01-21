dicionario = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(dicionario["brand"]) # Ford
print(dicionario)
# PEGAR ALGO
print( dicionario.get("year") ) # 1964
# PEGAR AS CHAVES 
chave = dicionario.keys()
print( chave ) # dict_keys(['brand', 'model', 'year'])
# RETORNA OS VALORES DE TODOS OS DICIONARIOS
print( dicionario.values() ) # dict_values(['Ford', 'Mustang', 1964])
# RETORNA CADA ITEM COMO UMA TUPLA
print( dicionario.items() ) # dict_items([('brand', 'Ford'), ('model', 'Mustang'), ('year', 1964)])
