from clases.Persona import Persona

class Docente(Persona):

    def __init__(self, id: int, nombre: str, altura: float, 
                 edad: int, apellido: str, cursos_a_cargo: list)->None:
        
        super().__init__(id, nombre, altura, edad, apellido)
        self.cursos_a_cargo = cursos_a_cargo

    def devolver_cursos(self) -> str:
        separador = " y "
        return f"{self.nombre} {self.apellido} da {separador.join(self.cursos_a_cargo)}"