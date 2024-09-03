from abc import ABC, abstractmethod

class Persona(ABC):
    """Clase que representa persona"""

    @abstractmethod
    def __init__(self, cedula, nombre, apellido):
        self.cedula = cedula
        self.nombre = nombre
        self.apellido = apellido

    @abstractmethod
    def __str__(self):
        return "%s: %s, %s" % (str(self.cedula), self.apellido, self.nombre)
        
class Alumno(Persona):
    def __init__(self, cedula, nombre, apellido, carrera):

        Persona.__init__(self, cedula, nombre, apellido)

        self.carrera = carrera

    def __str__(self):
        return Persona.__str__(self), f"Carrera: {self.carrera} "

if __name__ == '__main__':

    A1 = Alumno("45678","m", "f", "a")
    print(f"Sus datos son: {A1.__str__()}")