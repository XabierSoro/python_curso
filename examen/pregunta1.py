class Animal: #definimos la clase animal
    def __init__(self, patas, nombre):# Atributos
        self.patas=patas
        self.nombre=nombre

    def hacerRuido(self):
        print("WOF WOF")


class Perro (Animal):
    def __init__(self, patas, nombre, raza):
        super().__init__(patas, nombre)
        self.raza=raza

    def correr(self):
        print("Estoy corriendo")



class Pajaro(Animal):
    def __init__(self, patas, nombre):
        super().__init__(patas, nombre)

    def volar():
        pass




if __name__=="__main__": # Punto de entrada de nuestro programa

    perro1=Perro(4, "Lucho", "caniche")
    
    print(perro1.patas) # instanciamos un perro
    print(perro1.nombre)
    print(perro1.raza)    
    perro1.correr() #ejecutamos el método correr del perro
    perro1.hacerRuido()





