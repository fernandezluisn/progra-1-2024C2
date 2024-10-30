import copy

matriz_numeros = [[1, 55, 332, -9], [1, 2, 4, 66]]

matriz_numeros_b = matriz_numeros

deep_copy = copy.deepcopy(matriz_numeros)

# comparamos referencia en memoria
print(f"id original {id(matriz_numeros)}")
print(f"id matriz b {id(matriz_numeros_b)}")
print(f"id deep copy {id(deep_copy)}")

# comparamos referencia en memoria de las listas que la integran
print(id(matriz_numeros[1]))
print(id(deep_copy[1]))

deep_copy[0][0] = 90

# comparamos qué sucede con los valores dentro de los elementos que la componen al
# realizarse un cambio
print(matriz_numeros)
print(deep_copy)