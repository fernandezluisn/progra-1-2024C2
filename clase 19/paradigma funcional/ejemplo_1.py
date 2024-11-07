def sumar(num_1: int, num_2: int) -> int:
    """
    Esta función realiza una suma.
    Recibe dos enteros, devuelve un entero
    """

    return num_1 + num_2

operacion = sumar

print(id(sumar))

print(id(operacion))

print(operacion(1, 1))

def restar(num_1: int, num_2: int) -> int:
    """
    Esta función realiza una resta.
    Recibe dos enteros, devuelve un entero
    """

    return num_1 - num_2

operaciones = [sumar, restar]

for oper in operaciones:
    print(oper(3, 2))
