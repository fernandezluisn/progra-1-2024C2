archivo = open("./clase 19/archivos/archivos guardados/matriz.csv", "r")
texto = archivo.read()
archivo.close()

archivo = open("./clase 19/archivos/archivos guardados/matriz.csv", "r")
lista = archivo.readlines()
archivo.close()


print(texto)
print(lista)