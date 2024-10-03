def ordenar_x_burbujeo(lista: list) -> list:

    '''
    Recorre una lista y ordena elementos adyacentes.
    Recibe una lista.
    Devuelve una lista.
    '''

    if type(lista) != list:
        print("El parámetro de la función debe ser una lista")
        return None
    
    n = len(lista)

    for i in range(n):
        
        print(f"Iteración {i}")
        intercambio = False

        for j in range(0, n - i - 1):

            if lista[j] > lista[j + 1]:
                intercambio = True
                #print(f"Se intercambia {lista[j]} por {lista[j + 1]}")
                menor = lista[j + 1]
                lista[j + 1] = lista[j]
                lista[j] = menor
                print(lista)

        if intercambio == False:
            print(f"Dejó de correr en la iteración {i}")
            break

    return lista