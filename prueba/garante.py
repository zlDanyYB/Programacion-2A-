from agencia import agencia

class garante(agencia):
    color = str
    marca= str
    ruedas = str
    
    def __init__(self, nombre, apellido, edad, ruedas, color,marca):
        super().__init__(nombre,apellido,edad)
        
        self.color = color
        self.marca = marca
        self.ruedas = ruedas
        
agencia1 = agencia("Manuel","Perez", 35, 4, "Negro","Mazda")

print(vars(agencia1))