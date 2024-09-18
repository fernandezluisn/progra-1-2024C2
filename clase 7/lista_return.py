lista = [0] *5

# Se puede recibir listas por parámetro y devolver listas con return
def indexar_lista(lista:list)->list:
    
    if type(lista) == list: # es importante verificar que el elemento sea del tipo lista

        for i in range(len(lista)):
            lista[i] = i
    
    return lista

lista_resultado = indexar_lista(lista)

print(lista_resultado)