class Instrumento:
    def __init__(self, nombre, tipo, precio):
        self.nombre=nombre
        self.tipo=tipo
        self.precio=precio
        self.__preciocoste= precio -20 #preciocoste tiene 2 guiones bajos porque será un dato privado

    def tocar(self):
        print(f"{self.nombre} está tocando")


    

class Piano(Instrumento):
    def __init__(self, nombre, tipo, precio, teclas, musico):#constructor de Piano
        super().__init__(nombre, tipo, precio)#heredamos de la clase instrumento
        self.teclas=teclas
        self.musico=musico
    def tocar(self):
        print(f"{self.musico.nombre} está tocando el piano")# aquí hacemos el método para que imprima el músico asociado (jon) con el piano

class Musico:#hacemos una clase Musico
    def __init__(self, nombre):
        self.nombre=nombre


guitarra = Instrumento("Guitarra", "cuerdas", 100)#declaramos los atributos de guitarra

guitarra.tocar()#llamamos a la acción de tocar

jon=Musico("Jon")#instanciamos el músico Jon

piano1=Piano("piano X", "cuerdas-percusión", 100, 50, jon)
print(piano1.teclas)
piano1.tocar()#llamamos a la acción de tocar pero el del piano



