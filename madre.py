from hijo import Hijo
from Padre import Padre
from mascota import Mascota

class Madre(Padre):
    estudio = str
    enseña  = str
    hijo    = Hijo("", "" ,"")
    padre   = Padre("","","","","")
    mascota = Mascota("","","","")
    
    def __init__(self, nombre, apellido, edad, trabajo, coche, estudio, enseña, hijo, padre, mascota):
        super().__init__(nombre, apellido, edad, trabajo, coche)
        self.estudio = estudio
        self.enseña  = enseña
        self.hijo    = hijo
        self.padre   = padre
        self.mascota = mascota
madre1 = Madre("Maria","Carvajal","25","Profesora","MAZDA","UNIVERSIDAD CATOLICA", "Sociales",Hijo("Lucas","Erazo","13"),Padre("Manuel", "Erazo", "27", "Mecanico", "Chevrolet"),Mascota("Max","6","Pitbull","Macho"))

print(vars(madre1))
print(vars(madre1.hijo))
print(vars(madre1.padre))
print(vars(madre1.mascota))

class Madre2(Hijo,Mascota):
    idMadre = int
    hijo    = Hijo("", "" ,"")
    padre   = Padre("","","","","")
    mascota = Mascota("","","","")
    
    def __init__(self, nombre, apellido, edad, idMadre, hijo, padre, mascota):
        super().__init__(nombre, apellido, edad)
        self.idMadre = idMadre
        self.hijo    = hijo
        self.padre   = padre
        self.mascota = mascota
        
madre2 = Madre2("Sarita", "Fernandez", "26", 1 , Hijo("Jonathan","Fernandez", "17"),Padre("Xavier", "Chavez", "30","Ingeniero","Chevrolet"),Mascota("Max","6","Pitbull","Macho"))

print(vars(madre2))
print(vars(madre2.hijo))
print(vars(madre2.padre))
print(vars(madre2.mascota))