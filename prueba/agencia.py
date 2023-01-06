#CREACION DE UNA CLASE QUE CONTENGA EL METODO __str__
class Agencia:
    nombre   = str
    modelo   = int
    año      = str
    costo  = str
    
    def __init__(self, nombre, modelo, año, costo):
        self.nombre  = nombre
        self.modelo  = modelo
        self.año     = año
        self.costo   = costo

    def __str__(self):
        return f"El señor {self.nombre} adquirio su auto {self.modelo} el dia 25 de agosto del año {self.año} y el precio fue de:{self.costo} "
    
agencia1 = Agencia("Pepe", "Susuki", 2018, 13000)

print(agencia1)
