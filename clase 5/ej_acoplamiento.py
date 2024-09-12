# en este caso hay acoplamiento, ya que el correcto funcionamiento de calcular depende
# del correcto funcionamiento de restar. Como restar tiene un error de tipeo, calcular
# va a funcionar mal. 

# esta función está mal
def restar(num1: int, num2: int) -> float:
    return num1 / num2

# está función tiene un objetivo distinto ya que solo trabaja con enteros
def multiplicar(num1: int, num2: int) -> int:
    num1 = int(num1)
    num2 = int(num2)
    return num1 * num2

#La dependencia de calcular con las demás funciones genera que el programa arrastre errores.
def calcular(operacion: str, num1: float, num2: float) -> float:
    
    match operacion:
        case "resta":
            res = restar(num1, num2)
        case "multiplicacion":
            res = multiplicar(num1, num2)

    return res

resta = calcular("resta", 10, 5)
print(f"El resultado de restar 10 y 5 es {resta}")

multiplicacion = calcular("multiplicacion", 3.5, 5)

print(f"El resultado de multiplicar 3.5 y 5 es {multiplicacion}")

