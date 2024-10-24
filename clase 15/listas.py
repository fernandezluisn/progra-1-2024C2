lista_1 = [1, 3, 44]

lista_1.append(3)

print(lista_1)

lista_1.insert(1, 55)

print(lista_1)

lista_1.extend((6, 7))

print(lista_1)

lista_1.remove(3)

print(lista_1)

elemento_devuelto = lista_1.pop(1)

print(f"Se devolvió el {elemento_devuelto}")
print(lista_1)

print(lista_1.index(3))

lista_1.reverse()

print(lista_1)

lista_1.sort()

print(lista_1)


lista_1.sort(reverse = True)

print(lista_1)

del lista_1[2]

print(lista_1)

del lista_1[1:3]

print(lista_1)

lista_1.clear()

print(lista_1)

