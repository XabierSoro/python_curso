import requests

link = "http://info.cern.ch/"
r = requests.get(link)
print(r.status_code)
html=r.text# pasamos el texto, o código, html a la variable html
print(html)# hasta aquí hemos cogido el código html de la dirección web de la línea 3
html=html.replace("ch","eus")
html=html.replace("home","casa")
html=html.replace("Browse","Navegar")
html=html.replace("of","de")
html=html.replace("the","la")
html=html.replace("first","primera")
html=html.replace("website","página web")
print(html)# Hasta aquí hemos reemplazado palabras de ese código html para hacerlo local

#hemos imprimido este código html cambiado y lo hemos copiado y pegado en otro archivo de VS code guardándolo como .html
#después hemos arrastrado esta pestaña, la del html en Vs code, al navegador y vemos el cambio

