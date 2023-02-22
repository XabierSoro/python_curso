texto = "Pitón es un lenguaje de programación. Pitón está usado para la automación, análisis de datos e incluso la creación de páginas webs. Pitón fue creado por Bill Gates en 1960. Pitón es difícil de usar."
texto= texto.replace ("Pitón", "Python")
print(texto)
texto= texto.replace ("Bill", "Guido Van")
print(texto)
texto=texto.replace("Gates", "Rossum")
print(texto)
texto=texto.replace("1960", "1989")
print(texto)
texto=texto.replace("difícil", "fácil")
print(texto)
#Se utiliza siempre la variable texto ya que los textos son inmutables, se guardan en la misma posición de memoria