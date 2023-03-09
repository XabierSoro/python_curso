class Empleado:
    def __init__(self, nombre, apellido, puesto, pluspuesto, salariomin, nomina):
        self.nombre=nombre
        self.apellido=apellido
        self.puesto=puesto
        self.pluspuesto=pluspuesto
        self.salariomin= 950
        self.nomina=nomina

    def calcularnomina(self):
       self.nomina=(self.salariomin*1.2)

class Analista(Empleado):
    def __init__(self, nombre, apellido, puesto, pluspuesto, salariomin, nomina, rango):# En el constructor añado el rango, esto servirá para calcular el sueldo
        super().__init__(nombre, apellido, puesto, pluspuesto, salariomin, nomina)
        self.rango=rango
        

    def calcularnomina(self):
        self.nomina=(self.salariomin*self.pluspuesto) + self.rango # El plusrango será en función del rango del analista


class Programador(Empleado):
    def __init__(self, nombre, apellido, puesto, pluspuesto, salariomin, nomina, tipo): #aqui "tipo" será para definir si programa en python o java, y en función de esto cobrará más o menos
        super().__init__(nombre, apellido, puesto, pluspuesto, salariomin, nomina)
        self.tipo=tipo
       

    def calcularnomina(self):
        self.nomina=(self.salariomin*self.pluspuesto) + self.tipo # aqui el tipo será si es programador en python o java

def mostrar():    

    k=0
    while k< len(empleados):
        print(empleados[k].nombre)
        print(empleados[k].puesto)
        print(empleados[k].nomina)
        k+=1


empleados=[]



if __name__=="__main__":

    x=input("Desea ingresar un empleado? y/n ")   
    while x=="y":
        puesto=input("Elige la clase de empleado, Analista o Programador ")
        if puesto=="Analista":

            salariomin=950
            pluspuesto=1.1 #por ser analista          
            nombre=input("Introuce el nombre del empleado ")
            apellido=input("Introduce el apellido del empleado ")
            rango=input(f"Introduce el rango de {nombre} {apellido}: oficial ó peon ")
            nomina=0
            if rango=="oficial":
                rango=300
            else:
                rango=120   

            empleado=Analista(nombre, apellido, puesto, pluspuesto, salariomin, nomina, rango)
            empleados.append(empleado)
            empleado.calcularnomina()

        elif puesto=="Programador":
            salariomin=950
            pluspuesto=1.2
            nomina=0

            nombre=input("Introuce el nombre del empleado ")
            apellido=input("Introduce el apellido del empleado ")
            tipo=input(f"Introduce el tipo de {nombre} {apellido}: python o java? ")

            if tipo=="python":
                tipo=30000
            else:
                tipo=10  

            empleado=Programador(nombre, apellido, puesto, pluspuesto, salariomin, nomina, tipo)
            empleados.append(empleado)
            empleado.calcularnomina()
        x=input("Desea ingresar un empleado? y/n ") 
mostrar()