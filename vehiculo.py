class Vehiculo:

  def __init__(self, marca, modelo, tipo, fuel_maximo):
    self.marca = marca
    self.modelo = modelo
    self.tipo = tipo
    self.fuel_maximo = fuel_maximo
    self.__fuel_nivel = 1
    self.averiado = False


    def getSalario(self):
        return self._salario.upper()

    def setSalario(self, value):
        if value > 1000:
            self._salario = value

    @property
    def salario(self):
        return self._salario.upper()

    @salario.setter
    def salario(self, value):
        if value > 1000:
            self._salario = value


  def llenar(self):
    self.fuel_nivel = self.fuel_maximo
    print(f'El tanque ya esta lleno.{self.fuel_nivel}')


  def conducir(self):
    if self.averiado == True:
        print("No puedes conducir. Esta averiado")
    else:   
      self.fuel_nivel = self.fuel_nivel - 2
      if self.fuel_nivel <= 0:
        print("Lo siento, no te queda gasolina.")
      else:
        print(f'El {self.modelo} esta conduciendo.')

  def actualizar_deposito(self, nivel):
    if nivel <= self.fuel_maximo:
      self.fuel_nivel = nivel
    else:
      print('Demasiado gasonlina. Intentarlo de nuevo')

  def chocar(self):
    self.averiado=True
    print("ACCIDENTE")

  def accidente(self, otro):
    self.fuel_nivel = self.fuel_nivel - 5
    otro.fuel_nivel = otro.fuel_nivel - 5 


if __name__ == '__main__':
    rav4 = Vehiculo("Toyota", "rav4", "diesel", 100)
    ford = Vehiculo("Ford", "rav4", "gasolina", 100)
    rav4.conducir()
    rav4.chocar()
    rav4.conducir()
    rav4.accidente(ford)
    print(ford.fuel_nivel)