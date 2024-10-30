# constantes: son variables que no deben cambiar durante el ciclo de vida del programa

nombre_1 = "José"
NOMBRE = "Juan"

lisa = [1, 2, "Perro", True]
tupla = (1, 1.1, "Perro", True)

print(tupla)

# Si asigno un valor, devuelve error
#tupla[0] = 15

id, altura, especie, vacunado = tupla

print(f"El id es {id}")
print(f"La altura es {altura}")
print(f"La especie es {especie}")
print(f"Se encuentra vacunado: {vacunado}")

def convertir_centigrados_a_farenheit(grados_c: float) -> tuple:
    
    """
    Es una función que recibe grados centigrados y devuelve el equivalente 
    en grados farenheit y kelvin, junto al valor en centigrados.
    Recibe un Float.
    Devuelve una tupla.
    """

    farenheit = (grados_c * 9/5) + 32
    kelvin = grados_c + 273
    return (grados_c, farenheit, kelvin)

g_centigrados, g_farenheit, g_kelvin = convertir_centigrados_a_farenheit(22)

print(f"Hace {g_kelvin}° kelvin y {g_farenheit}° farenheit")

tupla_2 = (3, 3, 22, 1, 3, 3)
print(F"EL 3 APARECE {tupla_2.count(3)} veces")
print(F"El 22 está por primera vez en el índice {tupla_2.index(22)}")




