lista_numeros = [95, 3, 55, 4, 6, 9, 13, 12, 10, 99,
                 33, 22, 53, 44, 67, 69, 34, 19, 86, 100]

tam_cuartil = len(lista_numeros) // 4

maximos = [lista_numeros[0]] * tam_cuartil
minimos = [lista_numeros[0]] * tam_cuartil

for i in range(tam_cuartil):

    if i > 0:
        maximos [i] = minimos[0]
        minimos [i] = maximos[0]

    for j in range(len(lista_numeros)):

        if i > 0 and (lista_numeros[j] <= minimos[i-1] or 
                      lista_numeros[j] >= maximos[i-1]):
            print(f"Iteración {i} se saltea{lista_numeros[j]}")
            continue
        elif lista_numeros[j] > maximos[i]:
            maximos[i] = lista_numeros[j]
        
        if i > 0 and (lista_numeros[j] <= minimos[i-1] or 
                      lista_numeros[j] >= maximos[i-1]):
            continue
        elif lista_numeros[j] < minimos[i]:
            minimos[i] = lista_numeros[j]

        

print(maximos)
print(minimos)

