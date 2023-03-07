class Coche:
    def __init__(self, marca, modelo, tipo):
        self.marca=marca
        self.modelo=modelo
        self.tipo=tipo
        self.max=14
        self.min=0
        self.averia=False
    
    def conducir(self):
        print(self.max)
        if self.averia==True:
            print(f"Tu coche de marca {self.marca} está averiado después del accidente")
            print("Llévalo al taller para arreglarlo")

        elif self.max>=8:
            print("Disfruta, tienes gasolina de sobra")
            self.max=self.max-2

        elif self.max<8 and self.max>1:
            print("Puedes seguir pero tienes poca gasolina")
            self.max=self.max-2
        
        elif self.max<=0:
            print("No puedes conducir, estás sin gasolina")
        

       

    def llenardeposito(self):
        if self.max==14:
            print("Tienes el depósito lleno")
        elif self.max<14:
            self.max=self.max+4        

    def chocar(self):
        print("Has tenido un accidente, deberás llevar el coche al taller")
        self.averia=True
        
    def averiado(self):
        pass

    def taller(self):
        if self.averia==True:
            print("Tienes el coche averiado, te lo vamos a arreglar")
            self.averia=False
        else:
            print("Tienes el coche en perfectas coniciones, puedes seguir conduciendo")

if __name__=="__main__":
    v4=Coche("Seat", "Leon", "Diesel")

    v4.conducir()
    v4.conducir()
    v4.conducir()
    v4.taller()
    v4.conducir()
    v4.conducir()
    v4.conducir()
    v4.llenardeposito()
    v4.llenardeposito()
    v4.conducir()
    v4.conducir()
    v4.llenardeposito()
    v4.llenardeposito()
    v4.llenardeposito()
    v4.conducir()
    v4.conducir()
    v4.conducir()
    v4.conducir()
    v4.conducir()
    v4.chocar()
    v4.conducir()
    v4.taller()
    v4.conducir()
    v4.llenardeposito()
    v4.conducir()