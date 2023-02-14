accion = str(input("Teclea 'up' para sumar o 'down' para contar en negativo "))
if accion == "up":
    repeticion = int(input("cuantas veces quieres repetir? "))
    for i in range(repeticion):
        print(i)
elif accion == "down":
    repeticion = int(input("Cuantas veces quieres repetir? " ))
    for i in range(repeticion, 0, -1):# (empiezo, termino, el paso)
        print(i)
else:
    print("No has elegido correctamente")