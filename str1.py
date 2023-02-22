s = "    122,Python,es,64,un,777,lenguaje,222,de,55,66,programación"

s = s.strip()#elimina los espacios de la lista

print(s)

a=s.split(",")#nos separa todo en una lista
print(a)
print(type(a))#nos dice que es una lista
b=[str(i) for i in a if not i.isnumeric()]# me paseo por la lista, si no es numérico devuelvo el valor a i, así creo una lista con solo caracteres
#i.isnumeric() nos compara si es un número y nos devuelve un True o False
print(b)
texto_final="" # vamos a concatenar la lista con un espacio para que aparezca como una frase
texto_final = " ".join(str(i) for i in b)
print(texto_final)
print(texto_final.upper())# nos pone el texto en mayúscula