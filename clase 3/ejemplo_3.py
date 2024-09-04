lista_1 = [26, 45, 33, 67, 53, 59, 19, 37, 41, 32]
lista_2 = [33, 55, 777, 1234]
lista_3 = [331, 5533, 777, 1234]

producto = 1
def calcular_media_geo(lista):
    '''Calcula la enesima raíz del producto de todos los valores de la lista'''
    global producto
    print(producto)

    for numero in lista:
        producto *= numero

    resultado = producto ** (1/len(lista))
    print(resultado)

calcular_media_geo(lista_1) 
calcular_media_geo(lista_2)
calcular_media_geo(lista_3)