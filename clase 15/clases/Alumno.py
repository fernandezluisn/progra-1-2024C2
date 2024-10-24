from clases.Persona import Persona
from statistics import mean

class Alumno(Persona):
    
    def __init__(self, id: int, nombre: str, altura: float, 
                 edad: int, apellido: str, notas: list) -> None:
        
        super().__init__(id, nombre, altura, edad, apellido)
        self.notas = notas

    def retornar_promedio(self)->float:
        return mean(self.notas)