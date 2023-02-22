nombres = ["jon","maria", "juan", "javier"]# queremos sacar una lista con solo los que empiezan por J
nuevalista=[nombre for nombre in nombres if nombre[0]=="j"]
#el primer nombre del corche es lo que vamos a devolver a la nueva lista
#En el for, nombre va cogiendo cada valor de la lista nombres
#En el if ponemos la condición de que el primer caracter sea J
print(nuevalista)