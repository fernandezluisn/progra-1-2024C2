lista_a = [1, 2]

def mostrar_lista(una_lista: list) ->None:

    if type(una_lista) == list: # es importante verificar que el elemento sea del tipo lista
        for item in una_lista:
            print(item)
    else:
        print("La función debe recibir una lista")

mostrar_lista(2)