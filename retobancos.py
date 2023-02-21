accion = str(input("¿Tienes alguna transacción para introducir? (s/n)"))
count=0
total=0
count=0
cantidades=[] # Creamos la lista de cantidades
while accion == "s":
    transaccion=str(input("Teclee 'a' para ingresar dinero ó 'r' para retirar dinero "))
    if transaccion == "a":
        cantidad = float(input("Introduzca cantidad "))#nos pide la cantidad de la transacción
        cantidades.append(cantidad)# introducimos la cntidad en la lista de cantidades
        count=count+1 # Ponemos contador para conocer el numero de transacciones hechas y así poder hacer la media
        total=cantidad + total # Vamos sumando las transacciones
        accion = str(input("¿Tienes alguna transacción para introducir? (s/n)"))# volvemos a preguntar para salir o no del while
    elif transaccion == "r":
        cantidad = float(input("Introduzca cantidad "))#nos pide la cantidad de la transacción
        cantidad=cantidad*-1 # Ponemos la cantidad en negativo ya que es una retirada de dinero
        cantidades.append(cantidad)# introducimos la cntidad en la lista de cantidades
        count=count+1 # Ponemos contador para conocer el numero de transacciones hechas y así poder hacer la media
        total=cantidad + total # Vamos sumando las transacciones
        accion = str(input("¿Tienes alguna transacción para introducir? (s/n)" ))# volvemos a preguntar para salir o no del while
    else:
        print("no has seleccionado correctamente")
        accion=str(input("¿Tienes alguna transacción para introducir? (s/n)" ))

      
media=total/count
print(f"las transacciones realizadas son las siguientes {cantidades}")
print(f"La suma total de las transacciones es {total} €" )
print(f"La media de las transacciones es {media:.2f} € ")
suma=sum(cantidades)# Suma toda la lista de cantidades, por lo que no haría falta la variable total
print(f"la suma total de todas las transacciones es {suma} €" )