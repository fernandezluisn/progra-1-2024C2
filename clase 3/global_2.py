# ¿Por qué es una mala practica usar variables globales?

lista_1 = [26, 45, 33, 67, 53, 59, 19, 37, 41, 32]
lista_2 = [33, 55, 777, 1234]
lista_3 = [331, 5533, 777, 1234]

producto = 1
def calcular_media_geo(lista)->float:

    '''Calcula la enesima raíz del producto de todos los valores de la lista
    recibe una lista
    devuelve un float'''

    # Estoy cometiendo un error en el código. 
    # Ese error está asociado a la variable global 'producto'.    

    global producto
    print(producto)

    for numero in lista:
        producto *= numero

    resultado = producto ** (1/len(lista))
    print(resultado)

# Debido a que el error está asociado a una variable global, se esparce rapidamente.
calcular_media_geo(lista_1) 
calcular_media_geo(lista_2)
calcular_media_geo(lista_3)

# Imaginen esta situación en un programa de mayor escala