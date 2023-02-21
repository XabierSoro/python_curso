import random
alumnos=["Jon", "María", "Juan", "Asier"]
x = random.choice(alumnos) # Elegirá de forma aleatoria un elemento de la lista
if x == "María" or x=="Juan":
    print(f"{x} no está en clase")
elif x== "Asier" or x=="Jon":
    print(f"{x} si está hoy en clase")