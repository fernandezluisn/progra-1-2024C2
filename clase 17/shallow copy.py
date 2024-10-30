import copy

matriz_numeros = [[1, 55, 332, -9], [1, 2, 4, 66]]

matriz_numeros_b = matriz_numeros

shallow_copy = copy.copy(matriz_numeros)

print(f"id original {id(matriz_numeros)}")
print(f"id matriz b {id(matriz_numeros_b)}")
print(f"id shallow copy {id(shallow_copy)}")

print(id(matriz_numeros[1]))
print(id(shallow_copy[1]))

shallow_copy[0][0] = 90
matriz_numeros[0][1] = 60


print(matriz_numeros)
print(shallow_copy)

shallow_copy.append([1, 2, 3, 4])

print("Hacemos append")
print(matriz_numeros)
print(shallow_copy)
