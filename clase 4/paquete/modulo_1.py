# Creamos un módulo en el cual van a estar variables y funciones
# asociadas a la gestión de los estudiantes

# Para comunicar dos modulos de un paquete uso .
from .modulo_2 import UNIVERSIDAD

# Si está en mayúscula es una constante
MATERIA = "Programación 1"

# Una función es un bloque de código con una utilidad ESPECIFICA
# None significa que no devuelve nada. Se usa cuando no hay return 
# ya que no se devuelve objeto
def presentar_materia():
    print(f"Bienvenidos a {MATERIA} en {UNIVERSIDAD}")
    
def calcular_promedio(notas)->float:
    
    acumulador = 0
    contador = 0

    for nota in notas:
        acumulador += nota
        contador += 1

    promedio = acumulador / contador
    return promedio

# Evitar dependencia entre funciones
# Para aprobar hay que tener un promedio mayor a 6, 
# y no debe haber ninguna nota por debajo de 6
def estimar_aprobacion(lista_notas, promedio : float) -> str:     

    bandera = True

    # Para promocionar necesito que todas las notas sean mayores a 6
    for nota in lista_notas:
        if nota < 6:
            bandera = False
            break

    if promedio > 6 and bandera == True:
        return "Promocionó"
    if promedio > 6 and bandera == False:
        return "Aprobó. Ya que tiene más de 6 de promedio, pero tiene notas debajo de 6."
    elif promedio > 4:
        return "Aprobó"
    else:
        return "Desaprobó"