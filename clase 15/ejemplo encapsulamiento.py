from clases.Persona import Persona

datos_biometricos = "datos"
print(datos_biometricos)
datos_biometricos = "modificados"
print(datos_biometricos)

persona_1 = Persona(1, "Jorge", 1.74, 33, "Villalba", "datos biometricos")

persona_1.retornar_descripcion()
persona_1.apellido = "Pereyra"
persona_1.retornar_descripcion()

persona_1.__datos_biometricos = "modif"

print(persona_1.retornar_datos_biometricos())


