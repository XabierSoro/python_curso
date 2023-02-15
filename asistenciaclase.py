alumnos = ["Arturo", "Julio", "Dani"]
count = 0
for i in alumnos: # nos paseamos por la lista, i coge como valor el nombre de cada uno
    alumno = str(input(f"Está en clase {i} y/n? "))# alumno coge o la y ó la n
    if alumno == "y":# si la respuesa anterior es "y" suma uno
        count=count+1
print(f"hoy han venido {count} alumnos ")
print("fin")