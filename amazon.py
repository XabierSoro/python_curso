validar=False
nombre = input("Introduce tu nombre ")
l=len(nombre)
print(l)
while l<6:
    nombre = input("Introduce tu nombre, el nombre debe tener más de 5 caracteres ")
    l=len(nombre)
    print(l)

while validar == False:
    contrasena = input("Introduce tu contrasena, la contraseña debe tener más de 6 caracteres ")
    l=len(contrasena)
    print(l)
    if contrasena in ("password", "contraseña", "1234567"): #si la palabra código está en el texto, nos imprime la frase siguiente
        print("La contraseña es demasiado fácil")
    elif l<7:
        print("La contraseña es muy corta ")
    else:
        validar=True

print("Nombre y contraseña guardadas")
nombre= nombre.title()
print(f"Bienvenido {nombre}")  

