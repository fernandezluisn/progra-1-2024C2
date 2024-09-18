# Puedo crear listas de determinado tamaño usando el asterisco.
# En este caso es de 5 elementos
lista_nueva_4 = [0] * 5

print(lista_nueva_4)
print(id(lista_nueva_4[0]))
print(id(lista_nueva_4[1]))

# Puedo acceder a sus elementos mediante el indice
for i in range(len(lista_nueva_4)):
    lista_nueva_4[i] = i

print(lista_nueva_4)
