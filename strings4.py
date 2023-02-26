emails = ["jon.smith@microsoft.com", "maria.fernandez@microsoft.com", "david@microsoft.com", "isabel@microsoft.es","alfonso@gmail.com"]

texto_final = " ".join(str(i) for i in emails)#De esta manera se consigue separar cada elemento, entre ellos, por un espacio, convirtiéndolo en texto
print(texto_final)
texto_final=texto_final.replace(" ","@")#Cambio loss espacios por una @
print(type(texto_final))
print(texto_final)
a=texto_final.split("@")#Elimino las @ para separar los nombres por un lado y los dominios por otro
print(a)
listanombres=[]# Creamos la lista de nombres
v=len(a)# Miramos la longitud de la lista en la que los nombres están por un lado y dominios por otro
print(v)
for i in range(0, v, 2):# hacemos un for desde 0 hasta la longitud de la lista y que vaya de 2 en 2 para que solo me coja los nombres
    listanombres.append(a[i])#pasamos los nombres de la lista, ya que i va cogiendo esos valores y los colocamos en la nueva lista, listanombres
print (listanombres)

listadominios=[]# Creamos la nueva lista, listadominios
v=len(a)
print(v)
for i in range(1, v, 2):#hacemos un for desde 1 hasta el valor de la longitud de la lista a, y que vay de 2 en 2, para que coja los dominios.
    listadominios.append(a[i])
print (listadominios)
listaunica=[]#creamos una lista única donde colocaremos los dominios pero no todos, los repetidos no se colocarán en la lista
v=len(listadominios)
print(v)
[listaunica.append(dominio) for dominio in listadominios if dominio not in listaunica]#Dominio irá cogiendo cada valor de la lista donminios y los pasará a la listaunica si no está en la listaunica. De esta manera no colocará dominios repetidos
print(listaunica)
c= " ".join(str(i) for i in listanombres)
print(c)
c=c.replace(" ","@nazaret.eus, ")#Cambio los espacios por una @nazaret.eus,
print(c)
c=c.replace("alfonso","alfonso@nazaret.eus")
print(c)