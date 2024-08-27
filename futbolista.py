from persona import Persona
from deportista import Deportista

class Futbolista (Persona, Deportista):

    listaFutbolistas = []

    def __init__ (self, nombre, edad, altura, sexo, añosPracticando, golesMarcados, tarjetasRojas, piernaHabil):

        Persona.__init__(self, nombre, edad, altura, sexo)
        Deportista.__init__(self, "Futbol", añosPracticando)

        self.golesMarcados = golesMarcados
        self.tarjetasRojas = tarjetasRojas
        self.piernaHabil = piernaHabil
        
        Futbolista.listaFutbolistas.append(self)

    def getGolesMarcados (self):

        return (self.golesMarcados)
    
    def setGolesMarcados (self, goles):

        self.golesMarcados = goles
    
    def getTarjetasRojas (self):

        return (self.tarjetasRojas)
    
    def setTarjetasRojas (self, tarjetas):

        self.tarjetasRojas = tarjetas

    def getPiernaHabil (self):

        return (self.piernaHabil)
    
    def setPiernaHabil (self, pierna):

        self.piernaHabil = pierna

    def __str__ (self):

        return(f"Mi nombre es {self.nombre} soy profesional en el deporte {self.deporte} Tengo {self.edad} años de edad y llevo {self.añosPracticando} años en el deporte")

        


