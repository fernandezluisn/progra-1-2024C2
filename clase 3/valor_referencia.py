# ¿Qué sucede con la referencia de una variable dentro de una función?
def restar(numero_a: int, numero_b: int) -> int:
    
    '''
    La función realiza una resta
    recibe enteros
    devuelve un entero    
    '''

    print(id(numero_a))
    #Variables local: numero_b
    return numero_a - numero_b


restar(5, 1)

var_1 = 5

print(id(var_1))

restar(var_1, 1)

