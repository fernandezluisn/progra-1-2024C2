# Se define el nombre de la clase en CamelCase
class Persona:    

    def __init__(self, id: int, nombre: str, altura: float, 
                 edad: int, apellido: str, datos_biometricos: any) -> None:
        self.id = id
        # con guión bajo se define que un atributo es privado
        self.nombre = nombre
        self.altura = altura
        self.edad = edad
        self.apellido = apellido
        self.__datos_biometricos = datos_biometricos


    def retornar_descripcion(self) -> None:
        print(f"El nombre es {self.nombre} y el apellido {self.apellido}, la altura es {self.altura}")

    
    
    def retornar_datos_biometricos(self):
        return self.__datos_biometricos
    
