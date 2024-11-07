listado = [1,2,3,4,5,6,7,8,9]

# compresión de listas
filtrado = [num for num in listado if num % 3 != 0]

print(filtrado)

# Lo mismo pero con lambda
filtrado_lambda = list(filter(lambda x: x % 3 !=0, listado))

print(filtrado_lambda)
