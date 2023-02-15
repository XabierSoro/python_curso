compras =["Plátanos", "Manzanas", "Leche"]
compras.append("Galletas")# Añadimos Galletas a la lista
compras.append("Zumo")
print(compras)# Imprimimos toda la lista
print(compras[1:3])# Nos imprime el segundo y tercer elemento de la lista
print(compras[3:])# Nos imprime los dos últimos, el 4 y 3 ya que la lista es 0 1 2 3 4
compras[4] = "Zumo de Naranja" #Cambiamos zumo por Zumo de Naranja
print(compras)
compras.pop()#Elimina de la lista al último
print(compras)
compras.insert(2, "Limones")# nos inserta en la tercera posición los limones
print(compras)
compras.sort()# ordena alfabéticamente de forma ascendente
print(compras)
compras.sort(reverse = True)# ordena alfabéticamente de forma descendente
print(compras)