matriz = [[1, 3, 4], [4, 33, 5]]

with open("./clase 19/archivos/archivos guardados/matriz3.csv", "w") as archivo:

    for fila in matriz:
        linea = ""

        for i in range(len(fila)):
            linea += str(fila[i])

            if i < (len(fila) - 1):
                linea += ","
    
        archivo.write(linea + "\n")