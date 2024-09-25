from funciones.matrices import inicializar_matriz

def sumar_matrices(matriz_1: list, matriz_2: list) -> list:

    #controlo filas
    if len(matriz_1) == len(matriz_2):
        print("Son matrices de mismo orden")
    else:
        print("Las matrices deben tener misma cantidad de filas")
        return None
    
    #Controlo que la cantidad de columnas de todas las filas sea la misma
    for i in range(1, len(matriz_1)):
        if matriz_1[i] != matriz_1[i-1]:
            print("La matriz tiene que ser cuadrada")
            return None

    #controlo columnas
    for i in range(len(matriz_1)):
        if len(matriz_1[i]) !=  len(matriz_2[i]):
            print("Las matrices deben tener misma cantidad de columnas")
            return None

    matriz_respuesta = inicializar_matriz(len(matriz_1), len(matriz_2[0]))

    for fila in range(len(matriz_1)):
        for columna in range(len(matriz_1[fila])):
            matriz_respuesta[fila][columna] = matriz_1[fila][columna] + matriz_2[fila][columna]

    return matriz_respuesta

matriz_a =[[1, 2, 3], [2, 4], [3, 4, 5]]
matriz_b =[[1, 2, 6], [2, 4], [1, 1, 1]]

print(sumar_matrices(matriz_a, matriz_b))



    

    

    