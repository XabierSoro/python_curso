class Perro:
    def __init__ (self, _nombre, _raza, _altura): # Constructor, y debajo los atributos
        self.nombre=_nombre
        self.raza=_raza
        self.altura=_altura
    
    def comer(self):
        print(f" {self.nombre} está comiendo")
    def dormir(self):
        print(f" {self.nombre} está comiendo ")
    def ladrar(self):
        print(f" {self.nombre} está ladrando ")


perros=[]
if __name__=="__main__": # empezamos el programa principal
    nombre=input("Como se llama tu perro? ")
    raza=input("Indícame su raza  ")
    altura=input("me puedes decir su altura? ")
    perro= Perro(nombre, raza, altura)# pasamos a la variable perro el objeto perro con los atributos nombre, raza, y altura
    perros.append(perro)
    print(f" Tu perro {nombre} de {raza} y {altura} se ha inscrito correctamente")

    print(perros)

    perro.ladrar()






    
