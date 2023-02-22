texto = "    Lo más importante que nos ha mantenido en Python... bueno, hay 2 cosas importantes. Uno son las bibliotecas. La otra cosa que nos mantiene en Python, y esto es lo más importante, es facil de leer y entender. Cuando contratamos nuevos empleados. Solo digo, 'todo lo que escribas debe estar en python'. Sólo para que pueda leerlo. Y es increíble porque puedo ver desde el otro lado de la habitación, mirando su pantalla, si su código es bueno o malo. Porque un buen código de Python tiene una estructura muy obvia. Y eso hace que mi vida sea mucho más fácil        "
n=texto.count("Python")# contamos el número de veces que aparece la palabra python
n1=texto.count("python")
n2=n+n1
print(n2)
l=len(texto)# nos da el num de caracteres del texto
print(l)
v=texto.find("Python")# nos dice en que posición se encuentra Python
print(v)
z=texto.find("Python", 50, l)# nos dice en que posición se encuentra el segundo Python
z=z+50+v
print(z)
if "código" in texto: #si la palabra código está en el texto, nos imprime la frase siguiente
    print("La palabra código está en el texto")
print("fin")
texto= texto.replace ("Python", "PYTHON")# cambiamos Python por PYTHON en toda la lista
print(texto)
texto= texto.replace ("python", "PYTHON")
print(texto)
texto = texto.strip()#elimina los espacios al principio y final del texto
print(texto)
print(type(texto))#nos dice que tipo es texto
texto= texto.swapcase()
print(texto)