def imprimirmensaje(): # Esta sería la funcion
    print("Java es un lenguaje de programación")
    print("Me gusta Java")
#hasta aquí sería la función

imprimirmensaje()
#########################
def imprimirmensaje(lenguaje): # Esta sería la funcion
    print(f"{lenguaje} es un lenguaje de programación")#la primera palabra la dejamos como variable
    #hasta aquí sería la función

imprimirmensaje("Python")#Python pasará a lenguaje
imprimirmensaje("Java")# Java pasará a lenguaje
#######################################

def calculo(a):
    return a+a+a # retur para que nos devuelva la suma
# hastra aquí otra función
y=calculo(5)# y cogerá el valor de la funcion calculo, 5+5+5=15
print(y)