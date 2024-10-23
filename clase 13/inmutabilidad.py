cadena = "Perro"
x = 1
print(f"id de x = 1 {id(x)}")
x = "Asado"
print(f"id de x = asado {id(x)}")

print(id(cadena))
cadena[3] = "x"