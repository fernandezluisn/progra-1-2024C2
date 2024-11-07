matriz = []

with open("./clase 19/archivos/archivos guardados/matriz2.txt", "r") as archivo:    
    for linea in archivo:
        
        # split toma elementos de una cadena de texto separados por el elemento
        # que recibe como parametro. Si es csv, debe ser coma.
        # Si no puede ser cualquier separador que se seleccione
        valores = linea.split(";")

        fila = []

        for valor in valores:
            fila.append(int(valor))
        
        matriz.append(fila)

for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        print(f"fila = {i}, columna = {j}, valor = {matriz[i][j]}")
