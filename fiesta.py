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
