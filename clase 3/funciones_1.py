lista_1 = [26, 45, 33, 67, 53, 59, 19, 37, 41, 32]
lista_2 = [33, 55, 777, 1234]
lista_3 = [331, 5533, 777, 1234]


def calcular_media_geo(lista)->float:
    
    #Documento la función
    '''
    Calcula la enesima raíz del producto de todos los valores de la lista
    recibe un listado de enteros
    devuelve un Float
    '''

    # Utilizo variable local para inicializar
    producto = 1

    # Calculo el producto mediante un for
    for numero in lista:
        producto *= numero

    # Calculo enesima raíz
    resultado = producto ** (1/len(lista))
    print(resultado)

calcular_media_geo(lista_1) 
calcular_media_geo(lista_2)
calcular_media_geo(lista_3)


