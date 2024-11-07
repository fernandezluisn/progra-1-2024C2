lista = ["Jorge", "Marsupial", "Pera"]


def ordenar_por_longitud(cadena: str)->int:
    return len(cadena)

#lista.sort(key= ordenar_por_longitud)

# misma función pero com lambda
lista.sort(key = lambda cadena: len(cadena))

print(lista)


