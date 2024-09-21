
def buscar_lineal(lista: list, buscado: any) -> int:

    '''Realiza busqueda lineal sobre una lista.
    Recibe una lista y un elemento de cualquier tipo.
    Devuelve un entero con el índice que ocupa el elemento buscado.
    En caso de no encontrarlo, devuelve None.

    '''

    # Es importante la validación con las listas
    if type(lista) != list:
        print("El primer parametro debe ser una lista.") 
        return None

    # Busca uno a uno en los elementos de la lista
    for i in range(len(lista)):
        # Si lo encuentra retorna el índice
        if lista[i] == buscado:
            return i
    
    return None

def buscar_binaria(lista:list, buscado: int) -> int:

    '''Realiza busqueda binaria sobre una lista ordenada.
    Recibe una lista y un elemento de tipo entero.
    Devuelve un entero con el índice que ocupa el elemento buscado.
    En caso de no encontrarlo, devuelve None.
    '''
    inicio = 0
    final = len(lista) - 1

    if type(lista) != list:
        print("El primer parametro debe ser una lista.") 
        return None

    while inicio <= final:
        medio = (inicio + final) // 2

        if lista[medio] == buscado:
            return medio
        elif lista[medio] < buscado:
            inicio = medio + 1
        else: #lista[medio] > buscado
            final = medio - 1

    return None
