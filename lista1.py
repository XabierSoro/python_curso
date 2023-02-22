numeros = [3, 54, -12, 4, -67, 99, -120]
listapositiva = [numero for numero in numeros if numero>0 ]
#creo una nueva lista, listapositiva, con los números positivos
#el primer "numero" del corchete es lo que iré devolviendo a la nueva lista
# en el for, numero irá cogiendo cada valor de la lista números
# con el if solo pasarán los que sean mayor que cero
print(listapositiva)

numeros = [3, 54, -12, 4, -67, 99, -120]
listapositiva = [numero*2 for numero in numeros if numero>0 ]
#creo una nueva lista, listapositiva, con los números positivos
#el primer "numero" del corchete es lo que iré devolviendo a la nueva lista pero multiplicado por 2
# en el for, numero irá cogiendo cada valor de la lista números
# con el if solo pasarán los que sean mayor que cero
print(listapositiva)