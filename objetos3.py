class Coche:

    def __init__(self, marca, modelo, tipo):
        self.marca=marca
        self.modelo=modelo
        self.tipo=tipo
        self.max=14
        self.min=1
        self.averia=False

        
    
    def conducir(self):
        print("Estás conduciendo")
        print("Te has quedado sin gasolina")
        self.max=self.max-2
        print(f"Tu nivel de gasolina es de {self.max}")

    
    def llenardeposito(self):
        print("depósito lleno")
        self.max=14
        print(f"Tu nivel de depósito es de {self.max}, ya puedes continuar")
    def chocar(self):
        self.averia=True
    def averiado(self):
        self.averia=False
        print("El coche se te ha parado")
        print("Llama a la grúa")
        print(f"Ya puedes recoger tu {self.marca} {self.modelo} del taller")
        



if __name__=="__main__": # empezamos el programa principal

    rav4=Coche("Seat", "León", "diesel")
    rav4.averia=False# Esta es la forma de cambiar el atributo, con el nombre de Rav4
    rav4.marca="Ibiza" # Aqui cambiamos la marca del vehículo
    rav4.conducir() 
    rav4.conducir() 
    rav4.conducir() 
    rav4.conducir()     
    rav4.chocar()
    if rav4.averia==True:# Como es un atributo, utilizamos el rav4.averia
        rav4.averiado()

  
    
    rav4.conducir()
