# Ejemplo en el cual suponemos que administramos la materia progra 1

# El modulo se "trae" al main mediante la palabra reservada import
# Puedo usar alias con as
import paquete.modulo_1 as mod1

# Tenemos dos parciales y un tp. necesitamos calcular el promedio
# Lista de notas es una simulación
notas_juan = [5, 7, 9]
notas_nicolas = [8, 10, 9]

print(mod1.MATERIA)
mod1.presentar_materia()

# Asigno el objeto que devuelve la función a una variable
promedio_juan = mod1.calcular_promedio(notas_juan)
promedio_nicolas = mod1.calcular_promedio(notas_nicolas)

# Para tener la seguridad de que estoy pasando correctamente un parametro
# puedo pasarlo con el nombre del mismo.
aprob_juan = mod1.estimar_aprobacion(promedio = promedio_juan,
                                          lista_notas = notas_juan)

aprob_nicolas = mod1.estimar_aprobacion(notas_nicolas,promedio_nicolas)

print(f"El promedio de Juan es {promedio_juan}. {aprob_juan}")
print(f"El promedio de Nicolas es {promedio_nicolas}. {aprob_nicolas}")

