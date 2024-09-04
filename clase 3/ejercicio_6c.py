lista_edad = [26, 45, 33, 67, 53, 59, 19, 37, 41, 32]

contador = 0
suma_edades = 0

for edad in lista_edad:
    
    if edad <= 40:
        continue
    else:
        contador += 1
        suma_edades += edad

print(suma_edades / contador)