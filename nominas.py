class Empleado:
    def __init__(self, nombre, apellido, tlf, salariomin, plus):
        self.nombre=nombre
        self.apellido=apellido
        self.tlf=tlf
        self.plus=plus
        self.salariomin= 950

    def calcularnomina(self):
        nomina=self.salariomin*self.plus
