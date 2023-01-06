#HERENCIA ENTRE ARCHIVOS CREANDO UN METODO EN EL HIJO
from vehiculo import Vehiculo

class garante(Vehiculo):
    nombre = str
    apellido= str
    edad = str
    
    def __init__(self, nombre, apellido, edad):

        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
    
    def __str__(self):
        return f"El señor {self.nombre} con apellido {self.apellido} con la edad de {self.edad} sera la persona que sera llamada por un cobro que no sea ralizado"
        
garante1 = garante("Tomas","Perez", 40)

print(garante1)