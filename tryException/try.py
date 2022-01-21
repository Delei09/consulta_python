# The try block lets you test a block of code for errors.
# The except block lets you handle the error.
# The else block lets you execute code when there is no error.
# The finally block lets you execute code, regardless of the result of the try- and except blocks.
#RuntimeError, TypeError, NameError Existe esse 3 tipos de erro

x = 123
# CAIR NO TRY
try:
    print(x)
except ValueError as e :
    print("ERRO È ESSE" , e)
    print("VOU CAIR NO ERRO")
finally:
    print("AQUI SEMPRE PASSA")
#CAIR NO EXCEPT
try:
    print(dsadsaasx)
except :
    print("VOU CAIR NO ERRO")
finally:
    print("AQUI SEMPRE PASSA")
# CAIR EM UM DETERMINADO EXCEPT
try:
    raise RuntimeError("ESTOU LAMÇANDO ERRO")
except RuntimeError  as e :
    print( f"{e} esse é o erro" )
finally:
    print("AQUI SEMPRE PASSA")
