from comun.pedir import *#solo importo las librerías creadas en la carpeta commun.
from comun.calculos import *

if __name__=="__main__":
    v,b=pedirusuario()#llamo a la función de pedir al usuario 2 numeros
    print(v,b)# Enseño los dos números 
    c=sumar(v,b)# Llamo a la función sumar
    print(c)#imprimo el resultado
    z,x=pedirusuario()# vuelvo a llamar a la función de pedir 2 números
    s=restar(z,x)
    print(s)