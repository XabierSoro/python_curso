gente = int(input("Cuanta gente acudirá a la fiesta? "))
max = 5 # máximo de personas que pueden ir a la fiesta
if gente > max:
    print(f"Lo siento el número máximo de invitados es {max} ")
else:
    invitados = []# creamos una lista llamada invitados
    for i in range(gente):
        nombre = str(input(f"Necesito el nombre del invitado {i} ")) #pedimos el nombre de cada invitado
        invitados.append(nombre)# añade el nombre a la lista invitados
    for i in range(gente): 
        print("bienvenido a la fiesta " + invitados[i]) # Saca uno a uno los invitados de la lista
    print("fin")
print(len(invitados))#nos dice el número de elementos que contiene la lista
print(invitados.count("Juan"))# nos dice cuantos Juan hay en la lista
print(invitados[1])# nos imprime el seguundo elemento de la lista
print(invitados[-1])# nos imprime el último de la lista
print(invitados[:3])# nos imprime los primeros 3 
print(invitados[3:])# nos imprime los 3 últimos
invitados[2] = "Luis" # nos modifica el invitado número 3
print(invitados)
invitados.remove("Juan")# Borra el invitado Juan
print(invitados)
invitados.pop()#Elimina de la lista al último
print(invitados)