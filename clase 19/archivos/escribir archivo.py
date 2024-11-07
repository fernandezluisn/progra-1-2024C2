archivo = open("./clase 19/archivos/archivos guardados/ejemplo.txt", "w")
archivo.write("Linea 1\n")
archivo.write("Linea 2\n")
archivo.close()

archivo_2 = open("./clase 19/archivos/archivos guardados/ejemplo2.txt", "w") 
lineas_archivo = ["Linea 1\n", "Linea 2\n"]
archivo_2.writelines(lineas_archivo)
archivo_2.close()