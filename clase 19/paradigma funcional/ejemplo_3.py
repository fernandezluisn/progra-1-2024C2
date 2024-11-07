def sumar_cinco(numero: int) -> int:

    """
    Suma cinco a un entero.
    recibe un entero, devuelve un entero
    """

    return numero + 5


def retornar_operacion()->any:
    return sumar_cinco

suma = retornar_operacion()

print(suma(3))
