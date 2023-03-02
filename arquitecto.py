from comun.pedir import *
from comun.areas import *


if __name__=="__main__":
    v,b=pedirusuario()#llamo a la función de pedir al usuario 2 numeros
    print(v,b)# Enseño los dos números 
    resultado=metroscuadrados(v,b)# llamo a la función metroscuadrados que multiplicará v*b introducidos por el usuario
    print(f"El área es {resultado} m2")
