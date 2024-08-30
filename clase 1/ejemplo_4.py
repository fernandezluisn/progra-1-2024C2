#Qué es una variable en python

var = "año"
var_2 = "año"

# Posee 3 características
print(f"valor: {var}")
print(f"tipo: {type(var)}")
print(f"etiqueta: {id(var)}")

print("¿Son lo mismo una variable con un valor y su valor sin ser asignado?")
print(id("año") == id(var))

print(id(var_2) == id(var))

var = 33
print(f"valor: {var}")
print(f"tipo: {type(var)}")
print(f"etiqueta: {id(var)}")

print(id("año") == id(var))

var = "año"
print(f"etiqueta: {id(var)}")

# Existen dos tipos de variables primitivas que no son tan comunes

print(type(3 + 2j))
print(type(b"hola"))

var_num = "33"
print(var_num)
print(type(var_num))

# Puedo castear variables
var_num_cast = int(var_num)
print(type(var_num_cast))





