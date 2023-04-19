

lista=[5,3,12,-6,-3,1,6,8,-12] #Creamos la lista

for i in lista: # Creamos un ciclo for para que pase por toda la lista
    if i>0: # Si el número es mayor de 0 (positivo), imprime el número
        print(i)


for i in lista:
    if i==6: #Con el for miramos toda la lista hasta que llegue al número 6 que lo imprime con el mensaje siguiente
        print(f"Hola número {i} ")
    