lista_nueva_5 = [1, 2, 3, 4, 5]

# Podemos acceder solo a algunas posiciones utilizando indices generados con range
for i in range(0, 4, 2):
    print(i)
    print(lista_nueva_5[i]) 

# range(inicie posición 4, termine en i == 0, decreciendo en 1)
# Podemos recorrer la lista del final al principio
for i in range(len(lista_nueva_5) - 1, -1, -1):
    print(f"El indice es {i}")
    print(f"El valor es {lista_nueva_5[i]}")

# También podemos acceder a elementos de la lista contando los indices desde el final
# usando números negativos.
print(lista_nueva_5[-2])



