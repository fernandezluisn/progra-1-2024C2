lista_numeros = [22, 44, 11, 12, 143, 98]

# Nuevamente uso continue para filtrar casos

for num in lista_numeros:
    if num > 70:
        continue
    else: 
        print(num)