def inicializar_matriz(cant_filas: int, cant_columnas:int, valor_inicial:any = 0) -> list:

    matriz = []

    for _ in range(cant_filas):

        fila = [valor_inicial] * cant_columnas

        matriz += [fila]
    
    return matriz

def cargar_secuencialmente(matriz: list, tipo: str,
                           lista_1:list, lista_2:list) -> list:    
                
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            # tipos de operaciones: cantidad, ventas
            valor = int(input(f"Ingrese {tipo} de {lista_2[j]} en {lista_1[i]}: "))
            matriz[i][j] = valor
    
    return matriz


    