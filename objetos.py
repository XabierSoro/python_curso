
class persona: # clase

    def __init__(self, _nombre, _edad):#Este sería el constructor. Tenemos que pasar self para tener acceso a los atributos de la clase
        self.nombre = _nombre # atributos
        self.edad = _edad
        print("Estoy vivo")

    def hablar(self):# Esto sería una acción, un método
        print(f"Hola soy {self.nombre}")


jon= persona("Jon", 18)
print(jon.nombre)
print(jon.edad)
jon.edad = 35
print(jon.edad)
jon.hablar()# Llamamos a la acción, nos imprimirá ""Hola soy Jon"

maria = persona ("Maria", 40)
maria.hablar()
