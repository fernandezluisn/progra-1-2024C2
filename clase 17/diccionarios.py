diccionario_1 = {"Nombre": "Juan",
                 "Apellido": "Suarez",
                 "Edad": 33}

print(type(diccionario_1))

print(diccionario_1["Apellido"])

print(diccionario_1.keys())
print(diccionario_1.values())
print(diccionario_1.items())

for clave, valor in diccionario_1.items():
    print(f"En la clave {clave} el valor es {valor}")

print(hash("Nombre"))

# Se utilizan elementos inmutables como claves
diccionario_2 = {(1, 3): "Jorge",
                 "Apellido": "Perez",
                 "Edad": 17}

print(diccionario_2[(1, 3)])
