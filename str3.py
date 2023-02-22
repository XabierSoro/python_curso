x="hola/mundo/como/esta"
a=x.split("/") # separamos en una lista eliminado la barra /
print(a)
texto_final="" # vamos a concatenar la lista con un espacio para que aparezca como una frase
texto_final = " ".join(str(i) for i in a)# va paseándose por la lista "a" introduciendo un espacio entre cada palabra. i va cogiendo cada vez el valor siguiente de la lista
# join forma una cadena de caracteres con los elementos de una lista
print(texto_final)