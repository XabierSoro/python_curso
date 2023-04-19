def area(base,altura): #Creamos la función con las dos variables
    
    return base*altura # Decimos a la función lo que queremos que nos devuelva


if __name__=="__main__": # Punto de entrada de nuestro programa

    base=float(input("Introduce la base ")) # Preguntamos al usuario y declaramos la variable como Float
    altura=float(input("Introduce la altura "))

    resultado=area(base,altura)# Llamamos a la función
    print(f"El resultado del cáculo del área es {resultado}")