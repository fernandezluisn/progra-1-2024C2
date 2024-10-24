from clases.Persona import Persona
from clases.Docente import Docente
from clases.Alumno import Alumno

#Persona es una clase

# persona 1 es un objeto
persona_1 = Persona(1, "José", 1.74, 54, "Perez", "dato_1")
# persona 2 es otro objeto
persona_2 = Persona(2, "Juana", 1.65, 40, "Rodríguez", "dato_1")

# polimorfismo
print("POLIMORFISMO")
persona_1.retornar_descripcion()
persona_2.retornar_descripcion()

# docente_1 = Docente(3, "Jorge", 1.80, 45, "Suarez", ["matemática", "Estadística"])

# print(docente_1.cursos_a_cargo)
# docente_1.retornar_descripcion()
# print(docente_1.devolver_cursos())


# alumno_1 = Alumno(4, "Nicolas", 1.73, 20, "Mendoza", [9, 8, 6])
# print(f"el promedio de {alumno_1.nombre} es {alumno_1.retornar_promedio()}")

# for i in range(50):
#     persona = Persona(i, f"nombre {i}", 1 + (i * 0.02), i, "Rodríguez")
#     persona.retornar_descripcion()





