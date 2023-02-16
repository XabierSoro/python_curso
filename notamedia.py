notas = []
asignaturas = ["matemáticas", "historia", "biología", "inglés", "aleman", "python", "francés"]
total = 0
count = 0
for asignatura in asignaturas:# asignatura va cogiendo cada valor de la lista asignaturas
    nota = float(input(f"Indica la nota para la asignatura de {asignatura} "))# pregunta por la nota de cada asignatura
    notas.append(nota)# introducimos la nota en la lista de notas
for nota in notas:
    total = nota + total 
    count = count +1
media = total/count
print(f"tu nota media es de {media:.1f}")
