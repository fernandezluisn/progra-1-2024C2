#Las listas son mutables, y apuntan a un determinado espacio en memoria
# Si dos listas apuntan al mismo espacio y una de ellas cambia
# sucederá lo mismo con la otra

list_1 = [1]
list_2 = list_1
list_3 = [1]

print(f"id lista 1 {id(list_1)}")
print(id(list_2))

# A diferencia de los tipos primitivos, dos listas pueden tener el mismo contenido
# y apuntar a distintos espacios en memoria
print(f"id lista 3 {id(list_3)}")

print(f"Lista 2: {list_2}")

# cambio la list_1 y cambia list_2
list_1[0] = "Pepe"

print(f"Lista 2: {list_2}")
print(f"Lista 3: {list_3}")

print(f"{id(list_1)}")
print(id(list_2))

print(id(list_3))

