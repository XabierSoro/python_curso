import random
print(dir(random))# nos da la lista de las funciones que tiene el módulo random
x=random.random()# Nos dará de forma aleatoria un número entre 0 y 9.99999999
print(x)
y = random.randint(10,100)#elegirá un número aleaorio ente 10 y 100
print(y)
frutas = ["manzana", "plátano", "kiwi"]
z = random.choice(frutas) # Elegirá de forma aleatoria un elemento de la lista
print(z)