class Vehiculos:
    def __init__(self, marca, modelo, tipo, ruedas):
        self.marca=marca
        self.modelo=modelo
        self.tipo=tipo
        self.ruedas=ruedas
        self.fuelmax=150
        self.fuelact=1
        self.averiado=False
        self.color="naranja"

    def conducir(self):
        print("Estás conduciendo")

    def llenardeposito(self):
        print(f"Estás llenando el depódito de tu {self.marca}")
    
    def chocar(self):
        print(f" Tu {self.marca} ha tenido un accidente")
    def aceitemotor(self):
        print(f"Debes mirar el aceite motor de tu {self.marca} {self.modelo}")

class Camion (Vehiculos):
    def __init__(self, marca, modelo, tipo, ruedas, largura):
        super().__init__(marca, modelo, tipo, ruedas)#esto es lo que hereda de la clase Vehiculo
        self.largura=largura

    def dormir(self):
        print("Has llegado a tu límite de horas, debes descansar y parar tu {sef.nombre}")

    def transportar(self):
        print("Tienes que llevar los productos a Suecia")



class Moto (Vehiculos):
    def __init__(self, marca, modelo, tipo, ruedas, cadena, manillar):# Este es el constructor de la clase moto
        super().__init__(marca, modelo, tipo, ruedas,)#esto es lo que hereda de la clase vehiculo
        self.cadena=cadena
        self.manillar=manillar

    def caballito(self): # añadimos este método, el de hacer caballitos, ya que solo es propio de las motos y no de los camiones
        print(f"Con tu moto {self.marca} {self.modelo} de {self.ruedas} ruedas no se puede hacer caballito, puedes romper el manillar de {self.manillar} ")


if __name__=="__main__":

    camion1=Camion("Nissan", "cd5", "2 ejes", 8, 8000)
    camion1.conducir()# aquí se puede ver que los métodos también se heredan
    camion1.chocar()
    moto1=Moto("Honda", "Dylan", "automático", 2, "si", "hierro" )
    moto2=Moto("Honda", "Scoopy", "marchas", 3, "no", "acero")
    moto1.chocar()
    moto1.aceitemotor()
    camion1.aceitemotor()
    moto2.llenardeposito()
    camion1.dormir()# este método es propio de la clase camión, no es heredada de vehiculo
    moto2.caballito()






