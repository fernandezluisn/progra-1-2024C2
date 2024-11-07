matriz = [[1, 3, 4], [4, 33, 5]]

with open('./clase 19/archivos/archivos guardados/matriz4.csv', 'w') as archivo:
    
    for fila in matriz:
        for columna in fila:
            archivo.write(f'{columna},')
        archivo.write('\n')