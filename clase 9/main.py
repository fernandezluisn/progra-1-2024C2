from funciones.matrices import *

# matriz_numerica = [[2, 3, 6], [1, 7, 3], [2, 4, 8]]

# matriz_personas = [["Pedro", 23, True], ["Marcos", 66, False]]

# matruz_grande = matriz_numerica + matriz_personas


# matriz_numerica[2][1] = 66
# mostrar_matriz(matriz_numerica)

filas = int(input("Ingrese cantidad de filas: "))
columnas = int(input("Ingrese cantidad de columnas: "))

matriz_x_funcion = inicializar_matriz(filas, columnas, 0)
matriz_x_funcion = cargar_matriz_secuencialmente(matriz_x_funcion)
matriz_x_funcion = cargar_aleatoriamente(matriz_x_funcion)

mostrar_matriz(matriz_x_funcion)

buscar_lineal_matriz(matriz_x_funcion, 2)
