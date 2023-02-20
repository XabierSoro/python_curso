accion = str(input("¿Tienes alguna transacción para introducir? (s/n)"))
count=0
total=0
count=0
cantidades=[] # Creamos la lista de cantidades
while accion == "s":
    cantidad = float(input("Introduzca cantidad "))#nos pide la cantidad de la transacción
    cantidades.append(cantidad)# introducimos la cntidad en la lista de cantidades
    count=count+1 # Ponemos contador para conocer el numero de transacciones hechas y así poder hacer la media
    total=cantidad + total # Vamos sumando las transacciones
    accion = str(input("¿Tienes alguna transacción para introducir? (s/n)"))# volvemos a preguntar para salir o no del while
media=total/count
print(f"las transacciones realizadas son las siguientes {cantidades}")
print(f"La suma total de las transacciones es {total} €" )
print(f"La media de las transacciones es {media:.2f} € ")
suma=sum(cantidades)# Suma toda la lista de cantidades, por lo que no haría falta la variable total
print(f"la suma total de todas las transacciones es {suma} €" )
