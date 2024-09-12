# supongamos que estamos programando una calculadora

from ej_cohesion1 import *

num1 = float(input("Ingrese primer número: "))
num2 = float(input("Ingrese segundo número: "))
operacion = input("Ingrese operación a realizar: ")

# No voy a poder llamar a la función restar1 y usar los números 
# cargados previamente, por lo que no es cohesiva. La función restar2
# sí lo es.

match operacion:
    case "resta":
        restar2(num1, num2)

