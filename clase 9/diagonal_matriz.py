from funciones.matrices import inicializar_matriz, mostrar_matriz

matriz_nueva = inicializar_matriz(3, 3)

for i in range(len(matriz_nueva)):
    matriz_nueva[i][i] = 1

for i in range(len(matriz_nueva)):
    print(matriz_nueva[i][i])


mostrar_matriz(matriz_nueva)

