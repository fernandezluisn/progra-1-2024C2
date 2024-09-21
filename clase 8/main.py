from algoritmos_busqueda.funciones import *

lista_ejemplo = [1, 2, 4, 5, 6, 7, 8, 99]

indice = buscar_binaria(lista_ejemplo, 99)
indice = buscar_lineal(lista_ejemplo, 99)

# cantidad de iteraciones
# busqueda lineal = 8 
# busqueda binaria = 3

# Validar lo que recibo
if indice is None:
    print("El elemento no se encuentra en la lista")
else:
    print(f"El indice donde se encuentra el elemento es {indice}")